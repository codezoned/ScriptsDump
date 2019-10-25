import pyautogui

width, height = pyautogui.size()  # set width and height to your screen pixels.
print(pyautogui.position())  # get mouse position
pyautogui.click(
    100, 100, button="left"
)  # click left mouse at (100,100) similarly use .mouseUp(),.mouseDown(),.doubleClick() etc
pyautogui.scroll(400)  # scroll down 400
pyautogui.moveTo(
    500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad
)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.write(
    "Hello world!", interval=0.25
)  # Type with quarter-second pause in between each key.
pyautogui.press("esc")  # Simulate pressing the Escape key.
pyautogui.keyDown("shift")
pyautogui.write(["left", "left", "left", "left", "left", "left"])
pyautogui.keyUp("shift")
pyautogui.hotkey("ctrl", "c")  # pressed in succession like ctrl+c

# For taking Screenshot
im1 = pyautogui.screenshot()
im1.save("my_screenshot.png")
im2 = pyautogui.screenshot("my_screenshot2.png")
# locating image on screen

