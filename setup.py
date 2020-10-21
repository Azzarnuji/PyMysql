from app import main, db, cursor
import app
import sys
from os import system
from sys import platform
import os
print("Installing Depedencies\n"
      "Jika Di Windows Jalankan Script Ini Di CMD Windows Dengan Hak Akses Administrator")
input("Tekan Enter Untuk Lanjutkan")
if platform == "linux" or platform == "linux2":
    system('apt update&&apt install python3 python openssl ')
    system('pip install mysql-connector-python')
elif platform  == "win32":
    system('pip install mysql-connector-python')
main(db,cursor)