import pyautogui
import webbrowser
import random
import string
from  time import sleep

pyautogui.FAILSAFE = True

movemouse = 'mousebool'
rickroll = 'rickbool'
openapplications = 'openbool'
number = 0
maxopen = 'maxopen'
pausetime = 'pausebool'
movements = 0

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


if rickroll == True:
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


if movemouse == True:
        while movements < 50:
            pyautogui.moveTo(random.randint(0,1920), random.randint(0,1080), duration=0.1)
            movements = movements + 1
            print(movements)


if openapplications == True:
        while number < maxopen:
            sleep(3)
            pyautogui.hotkey("win")
            sleep(0.2)
            pyautogui.typewrite(randomword(1))
            sleep(0.3)
            pyautogui.hotkey("enter")
            sleep(0.3)
            number = number + 1
            
