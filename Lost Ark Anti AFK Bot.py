import time
import pyautogui

from random import randint


def ScreenSetup():
    res = pyautogui.size()
    if str(res) == "Size(width=640, height=480)":
        print("Using 640x480, Changing Randomx and Randomy")
        randomxbot = 286
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
        randomybot = 235
        randomytop = 1173
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
            elif timebot >= 4294967:
                print("This is to large of a time input!")
            else:
                timetop = int(input("Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): "))
                if timetop <= 0:
                    print("Must Type an Integer > 0")
                elif timetop <= timebot:
                    print("This should be not equal to or larger then the lowest amount in range")
                elif timetop >= 4294967:
                    print("This is to large of a time input!")
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
        print("Next Interaction Time: " + str(timeWait) + " second(s) or " + str(timeWait // 60) + " minute(s) (Integer Division Not Accurate Minute Representation)!")
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

def ButtonSetup():
    ButtonClickList = ['q','w','e','r','a','s','d','f']
    print("The Default Button Click List Is:")
    print(ButtonClickList)
    while True:
        try:
            menuCheck = str(input("Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ")).lower()
            if menuCheck == "y":
                while True:
                    try:
                        amountToAppendCheck = int(input("How Many Keys Would You Like To Add To The List: "))
                        for i in range(amountToAppendCheck):
                            keyInput = input("Please Press a Key or Write The Key, Such As 'space' and then press enter: ")
                            ButtonClickList.append(keyInput)
                        break
                    except ValueError:
                        print("Type Error: You Have Entered An Incorrect Type! Please Enter An Integer")
                break
            elif menuCheck == "n":
                break
            else:
                print("Input Error: Please Enter Either Y or N")
        except ValueError:
            print("Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N")
    return ButtonClickList

def ButtonClick(buttonSetup):
    ButtonClickList = buttonSetup
    RandomButtonChoice = randint(0,7)
    ButtonClick = ButtonClickList[RandomButtonChoice]
    pyautogui.press(ButtonClick)
    print("Button Clicked: " + ButtonClick)

'''
def QueueDetection():
    queueDetectionScreenshot = pyautogui.screenshot(region=(771,435, 373, 204))
    queueDetectionScreenshot.save(r"queueDetectionScreenshot.png")
    print("Screenshot Taken")
'''

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    retScreenSize = ScreenSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(2)
    buttonSetup = ButtonSetup()
    print("The Button Click List Is: ")
    print(buttonSetup)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(2)
    timeSleepSettings = TimeSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #QueueDetection()
    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        TimeSleep(timeSleepSettings)  
        MouseClick(retScreenSize)
        TimeSleep(timeSleepSettings)
        ButtonClick(buttonSetup)
