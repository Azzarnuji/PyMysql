from core import checkos as cs
import time
import mysql.connector
from mysql.connector import errorcode
import app
from app import *
db = mysql.connector.connect(
    host="gns2nd.ddns.net",
    port=3306,
    user="root2",
    password="root2",
    database="test"
    
)
cursor = db.cursor()
def read(db,cursor):
    read1 = "SELECT nama,nim,kelas,jurusan FROM mahasiswa"
    cursor.execute(read1)
    hasil = cursor.fetchall()
    panjang = len(hasil)
    if cursor.rowcount < 1:
        print("----Tidak Ada Data----")
        time.sleep(1)
    else:
        i=1
        for x in hasil:
            print("\n-------------")
            print(i,"Nama: "+x[0],"\n"," NIM: "+x[1],"\n"," Kelas: "+x[2],"\n"," Jurusan: "+x[3])
            i+=1
        input("Tekan Enter Untuk Lanjut")
        app.menu(db,cursor)