# Rhythmbox DRPC

A simple Discord Rich Presence script for **Rhythmbox** on Linux systems. Written in Python.
This script shows:
- Currently playing song + artist
- Playback timer
- Sleek icon

This was written in two afternoons.

---

## Requirements
- Linux system (tested on Ubuntu / GNOME)
- Python 3.10+
- Rhythmbox
- Discord
- `playerctl`
- `python3-venv`

---

## Setup

1. Clone the repo
```bash
git clone https://github.com/kuba743/rhythmbox-drpc.git
cd rhythmbox-drpc
```
2. Create or enter a Python virtual environment (this is an example one)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Create a Discord application
- __Go to:__ https://discord.com/developers/applications
- Create a new application: __The name should be what you want the header of your RPC say, for example:__ "Currently listening to"
- __Go to:__ assets/rhythmboxicon.png
- Copy rhythmboxicon.png
- __Go to:__ Discord Developer Portal GUI -> Rich Presence tab -> Rich Presence Assets -> "Add Image(s)"
- Upload rhythmboxicon.png: __The name should be: "rhythmbox", otherwise the icon will not work!__
- __Go to:__ Discord Developer Portal GUI -> Oauth2 tab
- Copy "Client ID" value
- __Go to:__ rhythmbox_drpc.py
- Find: "__CLIENT_ID__" value (line 5)
- Replace "yourclientid" with your Client ID from your Discord Application
4. Run
- For the script to run properly, it should be run under the Python VENV where `pypresence` is installed.

__Optionally, you can make this script run at the startup of Rhythmbox.__
1. Find and edit the start file for Rhythmbox  (other/older distros might have a different path)
```bash
cp /usr/share/applications/org.gnome.Rhythmbox3.desktop ~/.local/share/applications/
nano ~/.local/share/applications/org.gnome.Rhythmbox3.desktop
```
2. Find the "Exec=" line and edit it. Remember, you must use absolute paths.
```bash
Exec=bash -c 'source /path/to/venv/bin/activate && python /path/to/script.py & exec rhythmbox %U'
```
3. Save and exit

### Important notes

1. Discord does __not__ support dynamic album covers
2. A short delay after skipping/switching songs is normal
3. This all works because of MPRIS (playerctl). If you don't have it, this script won't work.

---

## License

### This is all on the MIT license.

