#this script is made for educational purposes only.
from time import sleep
import pyautogui

# the coordinates given here are strictly w.r.t my computer screen size and where i have placed my icons
# to find your own coordinates, read the pyautogui documentation: https://pyautogui.readthedocs.io/en/latest/
#you can also use coordinateFinder.py script to find your coordinates
x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6= 37,341,136,81,1093,553,1259,603,1659,124,1637,922


def openMeeting():
    #open chrome
    pyautogui.moveTo( x1, y1, duration=1 )
    pyautogui.doubleClick()
    sleep(2)
    #open google meet from bookmark bar
    pyautogui.moveTo( x2, y2, duration=1 )
    pyautogui.click()
    sleep(2)
    #open current lecture
    pyautogui.moveTo( x3, y3, duration=1 )
    pyautogui.click()
    sleep(12)
    #join the lecture
    pyautogui.moveTo( x4, y4, duration=1 )
    pyautogui.click()
    sleep(2)
    #open messagebox in current meeting
    pyautogui.moveTo( x5, y5, duration=1 )
    pyautogui.click()
    sleep(2)
    #cursor to the message box
    pyautogui.moveTo( x6, y6, duration=1 )
    pyautogui.click()
    sleep(2)

