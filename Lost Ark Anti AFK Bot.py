import time
import pyautogui

from random import randint


#def ScreenSetup():
    #print("Your Screen Size Is: " + str(pyautogui.size()))

def RandomTimeGen():
        randtime = randint(30, 120)
        return randtime

def TimeSleep():
        timeWait = RandomTimeGen()
        time.sleep(timeWait)

def RandomLocationGen():
        randomx = randint(382,1582)
        randomy = randint(181,903)
        return randomx,randomy

def MouseClick():
    randomlocval = RandomLocationGen()
    randomx = randomlocval[0]
    randomy = randomlocval[1]
    pyautogui.moveTo(randomx,randomy)
    pyautogui.click()
    print("Mouse Clicked At: (" + str(randomx) + "," + str(randomy) + ")")

def ButtonClick():
    ButtonClickList = ['q','w','e','r','a','s','d','f']
    RandomButtonChoice = randint(0,7)
    ButtonClick = ButtonClickList[RandomButtonChoice]
    pyautogui.press(ButtonClick)
    print("Button Clicked: " + ButtonClick)

if __name__ == "__main__":
    #ScreenSetup()
    while True:
        TimeSleep()  
        MouseClick()
        TimeSleep()
        ButtonClick()
