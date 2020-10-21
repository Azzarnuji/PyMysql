from core import select as rd
from core import insert as ins
from core import update as up
from core import delete as delt
from core import checkos as cs
from core import search as sr
import mysql.connector
from mysql.connector import errorcode
import time
db = mysql.connector.connect(
    host="gns2nd.ddns.net",
    port=3306,
    user="root2",
    password="root2",
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
            print("----Koneksi Ke Server Berhasil----")
        else:
            print("---Koneksi Gagal---")
        value = (name, pas)
        row = cursor.execute(query,value)
        result = cursor.fetchall()
        hasil = len(result)
        if hasil < 1 :
            print("----Username Salah----")
            cs.sys.exit()
        else:
            print("----Selamat Datang "+name+"----")
            time.sleep(0.3)
            menu(db,cursor)
    except KeyboardInterrupt:
        time.sleep(0.3)
        cs.sys.exit("\nCTRL-C Terdeteksi\nExit")
    menu(db,cursor)
def update_admin(db,cursor):
    update1ad = "SELECT * FROM admin"
    cursor.execute(update1ad)
    hasil = cursor.fetchall()
    for x in hasil:
        print("ID: "+str(x[0]),"\nUsername: "+x[1],"\nPassword: "+x[2])
def menu(db,cursor):
    try:
        print("---Selamat Datang Di Program CRUD---\n"
            "1. INSERT Data\n"
            "2. READ Data\n"
            "3. UPDATE Data\n"
            "4. DELETE Data\n"
            "5. SEARCH Data\n"
            "6. Update Data Admin\n"
            "Tekan Tombol CTRL-C Untuk Keluar Program")
        pil = input("Masukkan Pilihan Anda: ")
        if pil in ('1','2','3','4','5','6'):
            if pil == '1':
                ins.insert(db,cursor)
            elif pil == '2':
                rd.read(db,cursor)
            elif pil == '3':
                up.update(db,cursor)
            elif pil == '4':
                delt.delete(db,cursor)
            elif pil == '5':
                sr.search(db,cursor)
            elif pil == '6':
                system('python update-admin.py')
            else:
                print("Input Salah")
        else:
            print("Pilihan Tidak Ada")
    except KeyboardInterrupt:
        print("\nTerima Kasih :)\nExiting")
        time.sleep(0.3)
        cs.sys.exit()
        
if __name__ == "__main__":
    while (True):
        main(db,cursor)