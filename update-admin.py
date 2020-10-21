import mysql.connector
from mysql.connector import errorcode
import sys
from sys import platform
from os import system
import time
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="test"
    
)
cursor = db.cursor()
def main(db, cursor):
    try:
        name = input("Masukkan Username Database Anda: ")
        pas = input("Masukkan Password Database Anda: ")
        query = "SELECT * FROM admin WHERE username=%s AND passwd=%s "
        if db.is_connected:
            time.sleep(0.5)
            print("Koneksi Ke Server Berhasil")
        else:
            print("Koneksi Gagal")
        value = (name, pas)
        row = cursor.execute(query,value)
        result = cursor.fetchall()
        hasil = len(result)
        if hasil < 1 :
            print("Username Salah")
            sys.exit()
        else:
            print("Selamat Datang "+name)
            time.sleep(0.3)
            menu(db,cursor)
    except KeyboardInterrupt:
        time.sleep(0.3)
        sys.exit("\nCTRL-C Terdeteksi\nExit")

def menu(db,cursor):
    try:
        print("---Selamat Datang Di Program CRUD---\n"
            "1. INSERT Data Admin\n"
            "2. READ Data Admin\n"
            "3. UPDATE Data Admin\n"
            "4. DELETE Data Admin\n"
            "Tekan Tombol CTRL-C Untuk Keluar Program")
        pil = input("Masukkan Pilihan Anda: ")
        if pil in ('1','2','3','4'):
            if pil == '1':
                insert(db,cursor)
            elif pil == '2':
                read(db,cursor)
            elif pil == '3':
                update(db,cursor)
            elif pil == '4':
                delete(db,cursor)
            else:
                print("Input Salah")
        else:
            print("Pilihan Tidak Ada")
    except KeyboardInterrupt:
        print("\nTerima Kasih :)\nExiting")
        time.sleep(0.3)
        sys.exit()
        
if __name__ == "__main__":
    while (True):
        main(db,cursor)