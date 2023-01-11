import pyautogui
import pydirectinput
import time
from ctypes import *
from threading import Thread
import random

key = 0x6B # Numpad + (Add) https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
valid = False

def state():
    global valid
    while True:
        if cdll.user32.GetAsyncKeyState(key) & 0x8000:
            valid = not valid
            time.sleep(0.3)
        print("|State: ", valid, "     ", end="\r")
        time.sleep(0.005)

print('''
 ██▀███  ▓█████ ▓█████▄ ▓█████  ██▓███   ██▓     ▒█████ ▓██   ██▓    ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓█   ▀ ▓██░  ██▒▓██▒    ▒██▒  ██▒▒██  ██▒   ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██ ░▄█ ▒▒███   ░██   █▌▒███   ▓██░ ██▓▒▒██░    ▒██░  ██▒ ▒██ ██░   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌▒▓█  ▄ ▒██▄█▓▒ ▒▒██░    ▒██   ██░ ░ ▐██▓░   ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
░██▓ ▒██▒░▒████▒░▒████▓ ░▒████▒▒██▒ ░  ░░██████▒░ ████▓▒░ ░ ██▒▓░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░░ ▒░ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░   ██▒▒▒    ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ░ ░  ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░ ▓██ ░▒░    ▒░▒   ░   ░ ▒ ▒░     ░    
  ░░   ░    ░    ░ ░  ░    ░   ░░         ░ ░   ░ ░ ░ ▒  ▒ ▒ ░░      ░    ░ ░ ░ ░ ▒    ░      
   ░        ░  ░   ░       ░  ░             ░  ░    ░ ░  ░ ░         ░          ░ ░           
                 ░                                       ░ ░              ░                   
''')

print("|By survivalizeed\n|Configure the start/stop hotkey in this script\n|The Language has to be set to english\n|Only start when in deploy view\n|===================================")

stateT = Thread(target=state)
stateT.start()
while True:
    if(not valid):
        continue
    while True:
        depP = pyautogui.locateCenterOnScreen("deploy.png", grayscale=True, confidence=0.7)
        if depP is not None:
            break
        time.sleep(0.05)
    pyautogui.moveTo(depP)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pydirectinput.press("esc")      
    while True:
        redepP = pyautogui.locateCenterOnScreen("redeploy.png", grayscale=True, confidence=0.6)
        if redepP is not None:
            break
        time.sleep(0.05)
    pyautogui.moveTo(redepP)
    time.sleep(0.05)
    pyautogui.click()
