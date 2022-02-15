[![CodeQL](https://github.com/InfamyStudio/lostArkAntiAFKBot/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/InfamyStudio/lostArkAntiAFKBot/actions/workflows/codeql-analysis.yml)
# Lost Ark Anti AFK Bot
To tackle the issue of long queue times and harsh AFK timers I have created an Anti AFK Bot For Lost ARK

# Important Note
There is no known fact that EAC has an issue with CLI (Command Line Interfaces) being open when in a game
It is up to you if you choose to run the program!

# Latest Release
- Currently [V1.4](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V1.4) is the latest release available!
- Fixed Screen Res issue for float values
- prepping code for Queue Detection System also V1.4 Being Released Very Soon!

# Usage
## Usage ~ About
- I recommend using the obfuscated version of the project nicknamed "Obfuscated.py"
- I recommend changing the name of the program and burying it elsewhere on the file system
- I recommend going to a private area in Lost Ark and all you would need to do is boot up the program and switch back to Lost Ark
## Usage ~ Program Setup
- System automatically detects resolution and adjusts config accordingly
- System asks you to enter shortest/longest wait time to randomly select wait times between
- System asks you if you want to add more Buttons to the Click List
- You can choose to expand out the default buttons which are: ['q','w','e','r','a','s','d','f']
## Usage ~ Program Run time
- The system starts off with a mouse click at a random screen location cords within the clickable area of the game
- The system then presses a key which is randomly selected from the Buttons List (Either Default Or Custom)
- The system runs 30-120 seconds random time selection between each event
- The system selects a random key button every time of the array of "usable" buttons
- The systems selects a random screen coordinate to click every time
- The program runs indefinitely until closed and be careful not to run the program e.g. just on your desktop

# Release History
- [V1.4](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V1.4)
- [V1.3](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V1.3)
- [V1.2](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V1.2)
- [V1.1](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V1.1)
- [V1.0](https://github.com/InfamyStudio/lostArkAntiAFKBot/releases/tag/V1.0)

## Setup:
1) Firstly Install Python and make sure to install the package manager PIP (Do This In Admin Privileges in CMD etc)
2) Next in CMD run "pip install pyautogui" This installs the dependencies for the project
3) Now move the program into another drive preferably from the game and rename it to you choosing (bury this in a few random files)
4) Enjoy usage

## About:
- Built this program for a friend and the program currently is fully undetected and ready to go
- You are free to usage any script type above for example if you do not trust the Minified Code or Obfuscated Code.
- You can also run your own Obfuscation on the source code to better hide the program if you do worry about EAC (Easy Anti Cheat)
- Currently Macros have no definite answer on bans etc but generic rules state anything that is a bot or left unattended is breaking the rules
- Use at your own discretion!

## Plans for the future:
- EAC Bypass
- Create the program in multiple languages and different executables
- Possibly expand this project into a bot that interacts with the game better
- Add Queue detection (program only starts clicking etc when in game and not in Queue)

## Plans Completed:
- Add custom screen setup for all resolution types (Done)
- Add user input for selected wait times between inputs (Done)
- Add user input for selected keys to press (Done)
