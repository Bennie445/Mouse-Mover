import pyautogui
import sys
import os
import time
class color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'
print(color.CYAN)
print('███╗░░░███╗░█████╗░██╗░░░██╗░██████╗███████╗░░░░░░███╗░░░███╗░█████╗░██╗░░░██╗███████╗██████')
print('████╗░████║██╔══██╗██║░░░██║██╔════╝██╔════╝░░░░░░████╗░████║██╔══██╗██║░░░██║██╔════╝██╔══██')
print('██╔████╔██║██║░░██║██║░░░██║╚█████╗░█████╗░░█████╗██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░██████╔╝')
print('██║╚██╔╝██║██║░░██║██║░░░██║░╚═══██╗██╔══╝░░╚════╝██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗')
print('██║░╚═╝░██║╚█████╔╝╚██████╔╝██████╔╝███████╗░░░░░░██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗██║░░██║')

def mouse():
    start = input('Start the auto mouse-mover?')
    print('Made By Bennie')
    if start == 'yes' or 'start':
        print('SCRIPT HAS STARTED!')
        for i in range(840):
            pyautogui.moveTo(100,100, duration = 2)
            time.sleep(150)
            pyautogui.moveTo(1820,980, duration = 2)
            time.sleep(150)
while True:
    mouse()


