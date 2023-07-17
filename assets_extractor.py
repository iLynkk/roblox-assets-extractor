import os
import re
import shutil
import hashlib
import requests

home_directory = os.path.expanduser("~")
roblox_cache_path = os.path.join(home_directory, 'AppData', 'Local', 'Temp', 'Roblox', 'http')
roblox_sounds_cache_path = os.path.join(home_directory, 'AppData', 'Local', 'Temp', 'Roblox', 'sounds')
extracted_assets_output_path = os.path.join(home_directory, 'YOUR_OUTPUT_PATH_FOR_EXTRACTED_ASSETS')

already_extracted_assets = []

if not os.path.exists(extracted_assets_output_path):
    print(f"The following path: {extracted_assets_output_path} doesn't exist! Creating it...")
    os.makedirs(extracted_assets_output_path)

print(f"Initializing... Searching through assets cache path: {roblox_cache_path}")

for filename in os.listdir(roblox_cache_path):
    file_path = os.path.join(roblox_cache_path, filename)

    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="latin-1", errors="ignore") as file:
            file_content = file.read()

        match = re.search(r"https://[A-Za-z0-9]+\.rbxcdn\.com/([0-9]+([A-Za-z]+[0-9]+)+)", file_content)
        
        if match:
            link = match.group(0)

            try:
                response = requests.get(link)
                linked_file_content = response.content.decode("latin-1")

                content_checksum = hashlib.md5(response.content).hexdigest()

                if not content_checksum in already_extracted_assets:
                    if "<roblox!" in linked_file_content:
                        file_extension = ".rbxm"
                        print("Extracted RBXM file.")
                    elif "IHDR" in linked_file_content:
                        file_extension = ".png"
                        print("Extracted PNG file.")
                    else:
                        continue

                    with open(os.path.join(extracted_assets_output_path, f"{filename}{file_extension}"), "wb") as save_file:
                        already_extracted_assets.append(content_checksum)
                        save_file.write(response.content)
            except requests.exceptions.RequestException as e:
                print(f"Error fetching asset: {link}. Error message: {str(e)}")

print(f"Done. Searching through sounds cache path: {roblox_sounds_cache_path}")

for filename in os.listdir(roblox_sounds_cache_path):
    file_path = os.path.join(roblox_sounds_cache_path, filename)

    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="latin-1", errors="ignore") as file:
            file_content = file.read()

        if "OggS" in file_content:
            new_file_path = os.path.join(extracted_assets_output_path, os.path.splitext(filename)[0] + ".ogg")
            shutil.copyfile(file_path, new_file_path)
            
            print("Extracted OGG file.")
        elif "WAVE" in file_content:
            new_file_path = os.path.join(extracted_assets_output_path, os.path.splitext(filename)[0] + ".wav")
            shutil.copyfile(file_path, new_file_path)
            
            print("Extracted WAV file.")

print("Done. Finished extracting all assets.")
