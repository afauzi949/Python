''' Latihan Fungsi '''

import os

''' Biar lebih efisien menggunakan definisi fungsi '''



def header()->str:
    print(f"{'Selamat datang di Program':^40}")
    print(f"{'Menghitung Luas dan Keliling Persegi Panjang':^40}")
    print(f"{40*'=':^40}")

def inputan()->float:
    panjang:float = float(input("\nMasukkan Panjang : "))
    lebar:float = float(input("Masukkan Lebar   : "))
    return panjang,lebar

def luas(panjang:float,lebar:float):
    return panjang*lebar

def keliling(panjang,lebar):
    return 2*(panjang+lebar)

while True:
    os.system("cls")
    header()
    PANJANG,LEBAR = inputan()
    LUAS:float = luas(PANJANG,LEBAR)
    KELILING:float = keliling(PANJANG,LEBAR)
    print(f"Luas Persegi panjang = {LUAS}")
    print(f"Keliling Persegi panjang = {KELILING}")
    isContinue:str = input("\nApakah mau lanjut program(y/n) : ")
    if isContinue != "y":   
        print("\nTerima Kasih Telah Menggunakan Program\n")
        break