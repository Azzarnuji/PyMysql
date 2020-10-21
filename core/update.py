import app
from app import *
from core import checkos as cs
import time
def update(db,cursor):
    update3 = "SELECT nama,nim,kelas,jurusan FROM mahasiswa WHERE nim="
    update2 = int(input("Masukkan NIM Yang Ingin Di Update: "))
    update2str = str(update2)
    cursor.execute(update3+update2str)
    hasil3 = cursor.fetchall()
    if cursor.rowcount < 1:
        print("----Tidak Ada Data Untuk Di Update----")
        time.sleep(1)
        app.menu(db,cursor)
    for d in hasil3:
        print(" Nama: "+d[0],"\n","NIM: "+d[1],"\n","Kelas: ",d[2],"\n","Jurusan: "+d[3])
    um = input("Masukkan Update Nama: ")
    uk = input("Masukkan Update Kelas: ")
    update4 = "UPDATE mahasiswa SET nama=%s, kelas=%s WHERE nim=%s"
    uv = (um,uk,update2)
    cursor.execute(update4,uv)
    db.commit()
    print("----{} Data Berhasil Diubah".format(cursor.rowcount),"----")