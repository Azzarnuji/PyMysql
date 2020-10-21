import app
from app import *
from core import checkos as cs
import time
def search(db,cursor):
    nim = int(input("Masukkan NIM Yang Ingin Di Cari: "))
    search1 = "SELECT nama,nim,kelas,jurusan FROM mahasiswa WHERE nim="
    nimstr = str(nim)
    cursor.execute(search1+nimstr)
    hasil = cursor.fetchall()
    panjang = len(hasil)
    if cursor.rowcount < 1:
        print("----Tidak Ada Data----")
        time.sleep(1)
        app.menu(db,cursor)
    else:
        i=1
        for x in hasil:
            print("\n----Data Di Temukan----")
            print(i,"Nama: "+x[0],"\n"," NIM: "+x[1],"\n"," Kelas: "+x[2],"\n"," Jurusan: "+x[3],"\n")
            i+=1
        input("Tekan Enter Untuk Lanjut")
        app.menu(db,cursor)