# Roblox Assets Extractor
 This Python script extracts cached assets such as Images (PNG), Audios (OGG/WAV) and RBXM files from the Roblox cache folder.

 When you join a Roblox Experience, your client automatically caches Images and Audios in a temporary folder. You may want to clear that folder, which is located in `%Temp%/Roblox/http`, If you want to extract assets from a specific experience.

 If the `http` folder doesn't exist, you must manually create it in order for assets to be cached there.

## Requirements
- Python =< 3.11.0
- Windows (Operating System)
- Requests (Python Library)

### Initial Setup
- If you don't have Python, install it from [here](https://www.python.org/downloads/).
- Download the latest release, unzip it and delete `README.md`.
- Open a new Command Prompt, type: `pip install requests`
- Open and Edit the `assets_extractor.py` file, change `YOUR_OUTPUT_PATH_FOR_EXTRACTED_ASSETS` to the path where you want the extracted files to be saved. (example: `Downloads/extracted_assets`)

### Executing the Script
- Copy the path / location where the `assets_extractor.py` file is downloaded.
- Open a new Command Prompt and type: `cd PATH_HERE` and change `PATH_HERE` to the copied path.
- Then type `python assets_extractor.py` and the script will be executing.

**NOTE:** This script was made for the purpouse of checking which assets has been cached on your computer, because sometimes assets aren't cached and are missing in the Experience. Do not extract assets to infringe Intellectual Property or redistribute it, as that is agaisn't [Roblox Terms Of Service](https://en.help.roblox.com/hc/en-us/articles/115004647846).

**Recommended to use only on your OWN EXPERIENCES.**
