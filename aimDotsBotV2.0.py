"""
Game link : https://scratch.mit.edu/projects/285825495/
Put it in fullscreen
Run the python script
"""

import time
import keyboard
import pyautogui

time.sleep(1)
userInput = pyautogui.confirm(
    "Welcome to aimDotsBot, a bot made for Aim Dots© v1.19 by SoloOne\nFollow the procedure :"
    "\n1. Visit this link : https://scratch.mit.edu/projects/285825495/"
    "\n2. Put the project in fullscreen"
    "\n3. Launch the project by clicking on the green flag"
    "\n4. Press 'OK' to run the script"
    "\nThe bot plays independently. Press 'alt' button to pause/launch the process, press 'space' to stop the process...")

if userInput == "OK":
    # variables
    pyautogui.PAUSE = 0
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
    botRunning = True
    botToggle = True
    FPS = 30
    activeRegion = (384, 168, 1499, 976)
    diameter = 180
    precision = 10
    x, y = activeRegion[0], activeRegion[1]
    # (x=384, y=168)
    # (x=1499, y=976)

    # screenshot demo : pyautogui.screenshot("screenshot.png", region=screenShotRegion)

    # main loop
    while botRunning:
        # main script
        if botToggle:
            x += diameter - precision
            if x > activeRegion[2]-1:
                x = activeRegion[0]
                y += diameter - precision
                if y > activeRegion[3]-1:
                    y = activeRegion[1]
            # print(x, y)
            pyautogui.moveTo(x, y)

            # FPS manager
            if not FPS == 0:
                time.sleep(1 / FPS)

        try:
            if keyboard.is_pressed('alt'):
                botToggle = not botToggle
                while keyboard.is_pressed('alt'):
                    continue
            if keyboard.is_pressed('space'):
                botRunning = False
        except:
            print("Error : Something went wrong...")
            break
