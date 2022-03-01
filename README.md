[![CodeQL](https://github.com/InfamyStudio/lostArkAntiAFKBot/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/InfamyStudio/lostArkAntiAFKBot/actions/workflows/codeql-analysis.yml)
# Lost Ark Anti AFK Bot:
To tackle the issue of long queue times and harsh AFK timers I have created an Anti AFK Bot For Lost ARK

# Feature Set:
- Automatic Screen Resolution Detection (Changes Bot Click Area To Your Resolution!)
- Set shortest(30sec)/longest(1200sec) amount of time bot randomises between!
- Queue Detection - Screen Resolutions Supported For Queue Detection: 
```
- (All Widesreen-Resolutions should work) - Rest may work!
```
Queue Detection - Languages Supported For Queue Detection: 
```
    English              German
    French               Italian
    Turkish              Danish
```
- Auto Launches Character For You: (All Widesreen-Resolutions should work) - Rest may work!

# Want To Help The Project?
- Currently Queue Detection only has a few supported resolutions. What I need is gathered user data from all screen resolutions.
- Firstly download and setup https://github.com/mjdarby/ScreenCoordinateHelper
- Next record the exact cords for the "Waiting for server/queue" Box and record these details as follow:
```
- Top Left = Top left of box
- Top Middle = Top middle of the box
- Width = The top right which in turn doing Top left minus Top right gives us the width)
- Height = Top left of the box minus bottom left gives us the height.
```
- Please then record the screen coordinates for the centre of the "launch character" box.
- Lastly raise a GitHub issue with your screen resolution and the above details!

# Latest Release:
- Currently [2.8](https://github.com/Eaglescream/lostArkAntiAFKBot/releases/latest) is the latest release available!
- Update Queue Detection for more support on resolutions
- Updated README.md for how to get involved and help out

## Setup:
1) Download [Latest Release](https://github.com/Eaglescream/lostArkAntiAFKBot/releases/latest)
2) Start Exe

# Usage:
## Usage ~ About:
- You should use this program in a private location only accessible to you such as the Memory Chamber ideally
- You can change the name of the program and put it anywhere inside your file system to hide it further.
## Usage ~ Program Setup:
- System automatically detects resolution and adjusts config accordingly
- System asks you if you want to run Queue Detection (Use this if you are in a Queue, Currently Supported Widesreen-Resolutions - May work on others!)
- If you do run Queue Detection it will continuously keep checking the screen to see if you are in a Queue every 10 seconds! Even in Background NOT MINIMIZED!
## Usage ~ Program Run time:
- The system starts off with a mouse click at a random screen location cords within the clickable area of the game
- The system then presses a key which is randomly selected from the Buttons List 
- The system executes between mouse clicks and button presses between your random selected time frame
- The systems selects a random screen coordinate to click every time
- The system selects a random key button every time of the array of "usable" buttons
- The program runs indefinitely until closed and be careful not to run the program e.g. just on your desktop

# Release History:
- [V2.8](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V2.8) (Major Release(Patch))


## Plans for the future:
- Wait for feedback of Queue detection and resolve any issues and add more resolution support!
- Playing around with windows notifications and discord hooks!
- Possibly turning into a UI based program or offering both!

## About:
- Built this program for a friend and the program currently is fully undetected and ready to go
- You can use any version of the program as they are all the same always!
- You are free to use this code in your own projects and tamper with it as much as you like! If you make any cool changes let me know and I will merge it to main branch!
- You can also run your own Obfuscation on the source code to better hide the program if you do worry about EAC (Easy Anti Cheat)
- Currently Macros have no definite answer on bans etc but generic rules state anything that is a bot or left unattended is breaking the rules
- You are responsible for the usage of the program and anything that happens to your account is on you

