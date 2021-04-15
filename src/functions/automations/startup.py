import subprocess
import time
import pyautogui as p

p.PAUSE = 1
p.FAILSAFE = True


def startup():
    # opens Zoom, then Discord
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    time.sleep(10)
    subprocess.call(["/usr/bin/open", "/Applications/discord.app"])
    time.sleep(10)

    # clicks btn for Coding Dojo server in Discord
    d_btn = p.locateCenterOnScreen("<Insert path>")
    if d_btn is None:
        print("Image not found on screen.")
    else:
        p.moveTo(d_btn)
        p.click()
        time.sleep(2)

    # clicks link to Zoom classroom
    zoom_btn = p.locateCenterOnScreen("<Insert path>")
    if zoom_btn is None:
        print("Image not found on screen.")
    else:
        p.moveTo(zoom_btn)
        p.click()
        time.sleep(10)

    # opens Slack
    subprocess.call(["/usr/bin/open", "/Applications/slack.app"])