''' Latihan Fungsi '''

import os #impor modul OS

''' Biar lebih efisien menggunakan definisi fungsi '''

def header()->str:
    print(f"{'Selamat datang di Program':^40}")
    print(f"{'Menghitung Luas dan Keliling Persegi Panjang':^40}")
    print(f"{40*'=':^40}")

def inputan()->float:
    '''fungsi input'''
    panjang:float = float(input("\nMasukkan Panjang : "))
    lebar:float = float(input("Masukkan Lebar   : "))
    return panjang,lebar

def luas(panjang:float,lebar:float):
    '''fungsi luas'''
    return panjang*lebar

def keliling(panjang,lebar):
    '''fungsi keliling'''
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
        break
