# This program will help to find the coordinates of mouse cursor at a specific point
# You just need to run this program and move your cursor to the point where u want to find the coordinates
# Stop moving ur cursor for some time at that point and then quickly stop this python script.
# The most occured coordinates is the coordinates of ur point.


import pyautogui 
import time
while 1 :
    print(pyautogui.position())
    time.sleep(1)
