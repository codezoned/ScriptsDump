# automate opening an app using pyautogui

import pyautogui
pyautogui.locateOnScreen('C:\Users\Elio\Desktop\codezoned\ScriptsDump\Automation\src\Screenshots_and_image_recognition_using_pyautogui\u_torrent.PNG')
pyautogui.moveTo((1253,417), duration=3) #moves to icon in 3 seconds
pyautogui.click((1253,417), clicks=2) #opens icon in 2 clicks of left mouse button