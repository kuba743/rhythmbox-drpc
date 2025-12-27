import time
import subprocess
from pypresence import Presence

CLIENT_ID = "yourclientid"

# Give Discord time to start
time.sleep(5)

rpc = Presence(CLIENT_ID)
rpc.connect()

last_song = None

while True:
    try:
        status = subprocess.getoutput("playerctl status")

        if status != "Playing":
            rpc.clear()
            time.sleep(5)
            continue

        title = subprocess.getoutput("playerctl metadata title")
        artist = subprocess.getoutput("playerctl metadata artist")

        # Position in microseconds → seconds
        position = subprocess.getoutput("playerctl position")
        position = float(position)

        song_id = f"{artist}-{title}"

        # Reset timer when song changes
        if song_id != last_song:
            start_time = int(time.time() - position)
            last_song = song_id

        rpc.update(
            details=f"{title}",
            state=f"{artist}",
            start=start_time,
            large_image="rhythmbox"
        )

    except Exception:
        pass

    time.sleep(5)
