import time
import pyautogui

from random import randint


def ScreenSetup():
    res = pyautogui.size()
    if str(res) == "Size(width=640, height=480)":
        print("Using 640x480, Changing Randomx and Randomy")
        randomxbot = 286.5
        randomxtop = 351
        randomybot = 135
        randomytop = 301
    elif str(res) == "Size(width=1280, height=720)":
        print("Using 1280x720, Changing Randomx and Randomy")
        randomxbot = 573
        randomxtop = 702
        randomybot = 271
        randomytop = 602
    elif str(res) == "Size(width=1920, height=1080)":
        print("Using 1920x1080, Changing Randomx and Randomy")
        randomxbot = 382
        randomxtop = 1582
        randomybot = 181
        randomytop = 903
    elif str(res) == "Size(width=2560, height=1440)":
        print("Using 2560x1440, Changing Randomx and Randomy")
        randomxbot = 496
        randomxtop = 2056
        randomybot = 235.3
        randomytop = 1173.9
    elif str(res) == "Size(width=2048, height=1080)":
        print("Using 2048x1080, Changing Randomx and Randomy")
        randomxbot = 404
        randomxtop = 1676
        randomybot = 191
        randomytop = 957
    elif str(res) == "Size(width=3840, height=2160)":
        print("Using 3840x2160, Changing Randomx and Randomy")
        randomxbot = 744
        randomxtop = 3084
        randomybot = 286
        randomytop = 1759
    elif str(res) == "Size(width=7680, height=4320)":
        print("Using 7680x4320, Changing Randomx and Randomy")
        randomxbot = 1488
        randomxtop = 6168
        randomybot = 572
        randomytop = 3518
    else:
        print("Using Non-Supported Res, Changing Randomx and Randomy to Default Location!")
        print("Please raise an issue on GitHub with your screen res for future custom support!")
        randomxbot = 382
        randomxtop = 1582
        randomybot = 181
        randomytop = 903
    return randomxbot,randomxtop,randomybot,randomytop

def TimeSetup():
    print("Usage Just Type an Integer e.g. 30")
    while True:
        try:
            timebot = int(input("Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): "))
            if timebot <= 0:
                print("Must Type an Integer > 0")
            else:
                timetop = int(input("Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): "))
                if timetop <= 0:
                    print("Must Type an Integer > 0")
                else:
                    break
        except ValueError:
            print("Invalid Entry: Usage Just Type an Integer e.g. 30")
    return timebot,timetop

def RandomTimeGen(userTimeSettings):
        userSelected = userTimeSettings
        randtime = randint(userSelected[0], userSelected[1])
        return randtime

def TimeSleep(timeSleepSettings):
        userTimeSettings = timeSleepSettings
        timeWait = RandomTimeGen(userTimeSettings)
        print("Time Waiting Before Next Input: " + str(timeWait) + " second(s) or " + str(timeWait/60) + " minute(s)!")
        time.sleep(timeWait)

def RandomLocationGen(resScreenSize):
        screenSetup = resScreenSize
        randomx = randint(screenSetup[0],screenSetup[1])
        randomy = randint(screenSetup[2],screenSetup[3])
        return randomx,randomy

def MouseClick(retScreenSize):
    resScreenSize = retScreenSize
    randomlocval = RandomLocationGen(resScreenSize)
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
    retScreenSize = ScreenSetup()
    timeSleepSettings = TimeSetup()
    while True:
        TimeSleep(timeSleepSettings)  
        MouseClick(retScreenSize)
        TimeSleep(timeSleepSettings)
        ButtonClick()
