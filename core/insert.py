import app
from app import *
from core import checkos as cs
import time
def insert(db,cursor):
    nim = int(input("Masukkan NIM Mahasiswa: "))
    check = "SELECT nama, nim, kelas, jurusan FROM mahasiswa WHERE nim="
    nimstr = str(nim)
    cursor.execute(check+nimstr)
    hasil = cursor.fetchall()
    hasilstr = len(hasil)
    if hasilstr > 0 :
        for x in hasil:
            print("Data Sudah Ada Dengan :\n")
            print("Nama: "+x[0],"\nNIM: "+x[1],"\nKelas: "+x[2],"\nJurusan: "+x[3])
            print("\nSilahkan Input NIM Dengan Yang Lain\n")
            input("Tekan Enter Untuk Lanjutkan")
            app.menu(db,cursor)
    else:
        insert1 = "INSERT INTO mahasiswa (nama , nim, kelas, jurusan) VALUES (%s, %s, %s, %s)"
        print("--------------------")
        print("Masukkan NIM: "+nimstr)
        nama = input("Masukan Nama Mahasiswa: ")
        kelas = input("Masukkan Kelas Mahasiswa: ")
        jurusan = input("Masukkan Jurusan Mahasiswa: ")
        value1 = (nama, nimstr, kelas, jurusan)
        value2 = str(value1)
        cursor.execute(insert1,value1)
        db.commit()
        cs.check_os()
        print("----{} Data Berhasil Disimpan".format(cursor.rowcount),"-----")
    time.sleep(0.3)
    app.menu(db,cursor)

    app.menu(db,cursor)