# Perspective Transform
using puautogui methods
## How It Works
First take a screenshot of the icon or button of the application you want to click on and pass the location of the saved image to the code.
## Usage
use different modules and methods of pyautogui to automate your gui.

In this example I am trying to open uTorrent using pyautogui

Code:

```
pyautogui.locateOnScreen('C:\Users\Elio\Desktop\codezoned\ScriptsDump\Automation\src\Screenshots_and_image_recognition_using_pyautogui\u_torrent.PNG')
```
Locates the icon on the screen by finding the coordinates

```
pyautogui.moveTo((1253,417), duration=3)
```
Moves the pointer to the uTorrent icon in 3s

```
pyautogui.click((1253,417), clicks=2)
```
Opens uTorrent application in 2 automated clicks of the left mouse button 

See how it works from the gifs below:
### navigate to icon automatically
![Navigate to icon automatically](https://github.com/lopeselio/ScriptsDump/blob/Elio/Automation/src/Screenshots_and_image_recognition_using_pyautogui/navigate.gif)

### click on icon
![click icon to open the application](https://github.com/lopeselio/ScriptsDump/blob/Elio/Automation/src/Screenshots_and_image_recognition_using_pyautogui/click.gif)

