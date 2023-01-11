# Redeployer-BFV

### What is this?
####  This script was made for BFV to automatically redeploy your player so collect deaths

### Why would you want to use this?
#### FairFight checks your statistic and if it notices very suspicious stats it will likely ban you. This script will quickly reduce your K/D to stay under the ban limit

## This is only a little start. Fairfight does more than that...

Surely only reducing your K/D won't make you unbannable but still it goes in the right direction.  
If you then start to play without an ESP (even if it has Screenshot protection) and use an external radar instead you should be again a bit saver.
If you then don't only headshot everybody (for example with [Compound-V](https://github.com/survivalizeed/Compound-V)) and instead start to randomize your aim location 
you will be again saver.

### How does it work?
#### You might have noticed both the deploy.png and redeploy.png files. The script searches for both pictures and executes the actions written down in the script.

# How to use?

#### 1. Install python3 and add to path
#### 2. cmd.exe: pip install pyautogui
#### 3. cmd.exe: pip install pydirectinput
#### 4. cmd.exe: pip install Pillow
#### 5. cmd.exe: pip install opencv-python
#### 6. Launch bfV and turn on window borderless
#### 7. Go ingame and wait until you see the deploy view
#### 8. Open the Windows snipping tool and take a snip of the deploy button (like in the already existing deploy.png), save and replace with the deploy.png you got from here
#### 9. Deploy, press 'ESC' and take a snip of the redeploy button (like in the already existing redeploy.png), save and replace with the redeploy.png you got from here 
#### 10. The pictures now work for your current window size and your current resolution. If you change anything on the bfV window you need to redo from step 7.
#### 11. Start the script with a double click, go in deploy view and press the activate button (default is Numpad+)
#### 12. Done!

### Why do I have to take the pictures myself?
#### Because pyautogui makes a pixel compare and if you change the resolution the pixels will be different
