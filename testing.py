import pyautogui
import webbrowser
import random
import ctypes

movemouse = False
rickroll = False
openapplications = False


movements = 0

pyautogui.FAILSAFE = True

print(random.randint(0,100))

if rickroll == True:
        webbrowser.open('https://www.youtube.com/watch?v=069BsV5qn70&t=43s')


if movemouse == True
    while True
        if movements < 50:
            pyautogui.moveTo(random.randint(0,1920), random.randint(0,1080), duration=0.1)
            movements = movements + 1
            print(movements)
        if movements == 50:
            break
        
    

#input = pyautogui.prompt('This lets the user type in a string and press OK.')


#pyautogui.alert('This is an alert box.')


