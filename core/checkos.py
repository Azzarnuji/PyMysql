from app import *
import sys
from sys import platform
from os import system
def check_os():
    if platform == "linux" or platform == "linux2":
        system('clear')
    elif platform == "win32":
        system('cls')
    else:
        print("OS Not Compatible")