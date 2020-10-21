import app
from app import *
from core import checkos as cs
import time
def delete(db,cursor):
    delete1 = "SELECT nama,nim,kelas,jurusan FROM mahasiswa WHERE nim="
    delete2 = int(input("Masukkan NIM Yang Ingin Di Hapus: "))
    delete2str = str(delete2)
    cursor.execute(delete1+delete2str)
    hasil = cursor.fetchall()
    for x in hasil:
        print(" Nama: "+x[0],"\n","NIM: "+x[1],"\n","Kelas: ",x[2],"\n","Jurusan: "+x[3])
    tanya = input("Anda Yakin Ingin Menghapus??? Y/N: ")
    if tanya == 'Y' or tanya == 'y':
        delete3= "DELETE FROM mahasiswa WHERE nim="
        cursor.execute(delete3+delete2str)
        db.commit()
        print("{} data berhasil dihapus".format(cursor.rowcount))
        time.sleep(1)
        app.menu(db,cursor)
    elif tanya == 'N' or tanya =='n':
        app.menu(db,cursor)
    else:
        print("Input Salah")