# Roblox Assets Extractors
 This Python script extracts cached assets such as Images (PNG), Audios (OGG or WAV) and RBXM (may include Animations) from your computer.
 When you join a Roblox game, your client automatically caches images and audios in a temporary folder. You may want to clear that folder, which is located in `/AppData/Local/Temp/Roblox/http`, If you want to extract assets from a specific game.
 If the `http` folder doesn't exist you must manually create it.

## Requirements
- Python 3.11.0 or Higher
- Windows

### Setup
- If you don't have Python, [install it](https://www.python.org/downloads/).
- Open a Command Prompt, type: `pip install requests`
- Edit the `assets_extractor.py` file, and change `YOUR_OUTPUT_PATH_FOR_EXTRACTED_ASSETS` to the path where you want the extracted files to be saved. (example: "/Downloads/ExtractedAssets/")

### Executing
- Copy the path where the `assets_extractor.py` file is downloaded.
- Open Command Prompt and type: `cd PATH_HERE` and change `PATH_HERE` to the copied path.
- Then type `python assets_extractor.py` and it'll be running.

**NOTE:** This script was meant as a way to see which assets are being properly cached on your computer, as sometimes some assets aren't loaded or being cached. Do not extract assets to infringe Intellectual Property, as that is agaisn't [Roblox Term's Of Service](https://en.help.roblox.com/hc/en-us/articles/115004647846). Recommended to use it only on your **OWN EXPERIENCES**.
