import time
import pyautogui
import pytesseract
import os
import win32gui, win32com.client
import win32ui

from ctypes import windll
#import Image

import ctypes
user32 = ctypes.windll.user32
user = os.environ.get('USERNAME')
tesseractpath = 'C:/Users/' + user + '/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image
from PIL import ImageGrab
pytesseract.pytesseract.tesseract_cmd = tesseractpath
from random import randint

LAWindowTitle = "LOST ARK (64-bit, DX11) v.2.0.2.1" 

def ScreenSetup():
    WindowLocation = LALocation()
    randomxbot = WindowLocation[0] + round(1920*0.198958)
    randomxtop = WindowLocation[0] + round(1920*0.823958)
    randomybot = WindowLocation[1] + round(1080*0.16759259259259259)
    randomytop = WindowLocation[1] + round(1080*0.83611111111111111)
    launchx = WindowLocation[0] + round(1920*0.4453125)
    launchy = WindowLocation[1] + round(1080*0.9388888888888888888)
    scleft = 771
    sctop = 435
    scwidth = 373
    scheight = 204
    return randomxbot,randomxtop,randomybot,randomytop,launchx,launchy,scleft,sctop,scwidth,scheight

def TimeSetup():
    
    while True:
        try:
            #timebot = int(input("Please Enter The Shortest Amount of Seconds To Wait Before Input - Recommended (30 seconds): "))
            timebot = int(30)
            if timebot <= 0:
                print("Must Type an Integer > 0")
            elif timebot >= 4294967:
                print("This is to large of a time input!")
            else:
                #timetop = int(input("Please Enter The Longest Amount of Seconds To Wait Before Input - Recommended (1200 seconds): "))
                timetop = int(1200)
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

    print("The Shortest Amount of Seconds To Wait Before Input - 30 seconds")
    print("The Longest Amount of Seconds To Wait Before Input - 1200 seconds")
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

def LAForeground():
    #Bring to Foreground
    hwnd = win32gui.FindWindow(None, LAWindowTitle)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)
    #win32gui.ReleaseDC(hwnd)

def LALocation():
    if LAWindowTitle:
        hwnd = win32gui.FindWindow(None, LAWindowTitle)
        #print(hwnd)
        if hwnd:
            window_rect = win32gui.GetWindowRect(hwnd)
            #print(window_rect)
            LAleft = window_rect[0]
            LAtop = window_rect[1]
            LAwidth = window_rect[2] - LAleft
            LAheight = window_rect[3] - LAtop
            return LAleft,LAtop,LAwidth,LAheight
            
        else:
            print('Window not found!')

def MouseClick(retScreenSize):
    LAForeground()
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
            #menuCheck = str(input("Would You Like To Add More Keys To The ButtonClickList? Enter (Y) or (N): ")).lower()
            menuCheck = str("n").lower()
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
                amountToAppendCheck = 0
                break
            else:
                print("Input Error: Please Enter Either Y or N")
        except ValueError:
            print("Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N")
    return ButtonClickList,amountToAppendCheck

def ButtonClick(buttonSetup):
    LAForeground()
    ButtonClickList = buttonSetup[0]
    ButtonClickTop = buttonSetup[1] + 7
    RandomButtonChoice = randint(0,ButtonClickTop)
    ButtonClick = ButtonClickList[RandomButtonChoice]
    pyautogui.press(ButtonClick)
    print("Button Clicked: " + ButtonClick)

def screenshot(window_title=None):
    #Crop Location
    scleft = retScreenSize[6]
    sctop = retScreenSize[7]
    scwidth = scleft + retScreenSize[8] 
    scheight = sctop + retScreenSize[9] 
    #Window Rect
    hwnd = win32gui.FindWindow(None, LAWindowTitle)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    im = im.crop((scleft,sctop,scwidth,scheight))
    
    return im

def QueueDetection(retScreenSize):
    launchx = retScreenSize[4]
    launchy = retScreenSize[5]
    scleft = retScreenSize[6]
    sctop = retScreenSize[7]
    scwidth = retScreenSize[8]
    scheight = retScreenSize[9]
    while True:
        try:
            print("Make Sure Nothing is covering your lost ark window, specifficaly the Queue Box!")
            menuCheck = str(input("Would You Like To Start Queue Detection? Enter (Y) or (N): ")).lower()
            if menuCheck == "y":
                    try:
                        while True:
                            queDetectionTestScreenshot=screenshot(LAWindowTitle)
                            queDetectionTestScreenshot.save(r"queueDetectionScreenshot.png")
                            path = 'queueDetectionScreenshot.png'
                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Lost Ark Screen Being Analysed")
                            time.sleep(1)
                            queueDetect = pytesseract.image_to_string(Image.open(path))
                            if 'Waiting' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            elif 'Warten' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            elif 'Venter' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)                            
                            elif 'Attendre' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            elif 'In attesa' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9) 
                            elif 'Bekleme' in queueDetect:
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Still in Queue :(")
                                print("~Waiting 10 Seconds To Reanylse Screen!")
                                print("Sit Tight!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(9)
                            else:
    
                                print("Out of Queue! :)")
                                print("Waiting 60 seconds to launch your character!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                time.sleep(60)
                                
                                LAForeground()

                                pyautogui.moveTo(launchx,launchy)
                                pyautogui.click()
                                print("Mouse Clicked At: (" + str(launchx) + "," + str(launchy) + ")")
                                print("Character Launch In Progress!")
                                print("30 Second Wait Time!")
                                time.sleep(30)
                                break
                        break
                    except ValueError:
                        print("Type Error: You Have Entered An Incorrect Type! Please Enter An Integer")
            elif menuCheck == "n":
                break
            else:
                print("Input Error: Please Enter Either Y or N")
        except ValueError:
            print("Type Error: You Have Entered An Incorrect Type! Please Enter Either Y or N")
    

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    retScreenSize = ScreenSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    buttonSetup = ButtonSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    time.sleep(1)
    timeSleepSettings = TimeSetup()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    QueueDetection(retScreenSize)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        TimeSleep(timeSleepSettings)
        MouseClick(retScreenSize)
        TimeSleep(timeSleepSettings)
        ButtonClick(buttonSetup)
