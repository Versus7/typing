#imports
import time
import random
import pyautogui
import pytesseract
from PIL import ImageGrab
from PIL import Image

#functions

def typing(x,x2,y,y2):
    if x >= x2 or y >= y2:
        print("Check your values.")
    else:
        time.sleep(3)
        filepath = "typing.png"
        screenshot = ImageGrab.grab(bbox=(x,y,x2,y2))
        screenshot.save(filepath)
        screenshot.show()
        text = pytesseract.image_to_string(screenshot)
        print(text)

#preset 1: monkeytype
x, x2, y, y2 = 500, 2600, 1450, 1750


#execution
typing(x, x2, y, y2)
