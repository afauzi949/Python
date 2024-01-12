# deklarasi fungsi
def f(x):
    return x+1

y = f(4)
print(y)

# fungsi dengan parameter opsional
def makan(jumlah,harga = 20000):
    total = jumlah * harga
    return total

bayar = makan(3)
print(f"Total bayar makan adalah Rp{bayar:,}")

bayar = makan(3,30000)
print(f"Total bayar makan adalah Rp{bayar:,}")

# lebih 1 parameter 
def luas_trapesium(ss_atas,ss_bawah,tinggi):
    luas = 0.5 * (ss_atas+ss_bawah) * tinggi
    return luas

# urutan parameter
luas1 = luas_trapesium(2,5,7)
print(f"Luas Trapesium 1 adalah {luas1}")

# keyword argument
luas2 = luas_trapesium(tinggi=4,ss_atas=2,ss_bawah=6)
print(f"Luas Trapesium 2 adalah {luas2}")

# positional-only
def ucapan(nama,pesan,/):
    return f"Halo {nama}, {pesan}"

print(ucapan("Dudung","Selamat Pagi"))

# Keyword only
def greeting(*, nama, pesan):
    return f"Halo, nama saya {nama}. {pesan}"
 
print(greeting(pesan="Selamat datang!", nama="Bapak Fajar"))

# Var-positional
def ucapan(*args):
    return f"Halo {args[0]}, {args[1]}"

print(ucapan("Dudung","Mantap sekali"))

# Var keyword
def ucapan(**kwargs):
    return f"Haloooo,Saya {kwargs['nama']}.{kwargs['pesan']}"

print(ucapan(pesan="Mantap njay",nama="dudung"))

print("\nProsedur tidak mengembalikan nilai\n")
# Prosedur = tidak mengembalikan(return) suatu nilai
def makan(food):
    print(f"Aku makan {food}")

valueProcedure = makan("Seblak")
print(f"Fungsi makan mengembalikan nilai {valueProcedure}")
print(f"Value dari fungsi food adalah {type(valueProcedure)}")

print("\nAnotasi pada fungsi dan prosedur\n")
# Anotasi pada fungsi dan prosedur
def bayar_makan(jumlah:int ,harga:int =13000) ->int:
    totalbayar:int = jumlah * harga
    return totalbayar

total:int = bayar_makan(5,12000)
print(__annotations__)
print(bayar_makan.__annotations__)

def bayar_makanan(jumlah: int, harga_per_porsi: int = 10000) -> int:
    total_bayar: int  = jumlah * harga_per_porsi
    return total_bayar

total = bayar_makanan(2, 13000)   # anotasi variabel total dihilangkan

print(__annotations__)
print(bayar_makanan.__annotations__)

def eatSomething(food: str) -> None:     # diberikan anotasi None pada prosedur
    print(f"Saya sedang makan {food}.")
    return
 
eatSomething("Mi Ayam")

def eatSomething(food: str):     # tidak perlu anotasi pada prosedur
    print(f"Saya sedang makan {food}.")
    return
 
eatSomething("Mi Ayam")
 
# Quiz 1
print("\nQuiz\n")


"""
TODO:
 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel panjangRuang.
 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel lebarRuang.
 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel tinggiRuang.
 4. Buatlah fungsi bernama hitungCat yang memiliki parameter panjangRuang, lebarRuang, dan tinggiRuang.
    4.1. Hitung keliling ruangan dengan rumus keliling persegi panjang dan simpan pada variabel kelilingRuang.
    4.2. Hitung jumlah liter cat yang akan dipakai dengan rumus di atas.
    4.3. Fungsi ini mengembalikan nilai float yang menyatakan jumlah liter cat berdasarkan ketiga nilai tersebut.
    4.4. Simpan hasil fungsi pada variabel jumlahLiter.
 5. Cetak nilai jumlahLiter pada teks "Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter."
"""

# Tulis kode Anda di bawah ini

panjangRuang:float = float(input("Masukkan panjang ruangan : "))
lebarRuang:float = float(input("Masukkan lebar ruangan : "))
tinggiRuang:float = float(input("Masukkan tinggi ruangan : "))

def hitungCat(panjangRuang:float, lebarRuang:float, tinggiRuang:float) ->float:
    kelilingRuang:float = 2 * (panjangRuang+lebarRuang)
    jumlahLiter:float = kelilingRuang * (tinggiRuang/12)
    return jumlahLiter

jumlahLiter:float = hitungCat(panjangRuang,lebarRuang,tinggiRuang)
print(f"Jumlah cat yang Anda perlukan adalah {jumlahLiter} liter.")

print("\nQUIZ 2\n")

"""
TODO:
 1. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel landArea.
 2. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel width.
 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data float dan simpan pada variabel length.
 4. Buatlah fungsi bernama checkArea yang memiliki parameter landArea, width, dan length.
    4.1. Hitung luas bangunan dengan mengalikan variabel width dan length serta simpan pada variabel buildingArea.
    4.2. Periksa nilai buildingArea dan landArea dengan kriteria berikut.
         4.2.1. Apabila nilai buildingArea lebih besar dari landArea, kembalikan nilai False.
         4.2.2. Apabila nilai buildingArea kurang dari atau sama dengan landArea, kembalikan nilai True.
    4.3. Fungsi ini mengembalikan nilai boolean yang menyatakan bisa atau tidak bangunan dibangun berdasarkan ketiga nilai tersebut.
    4.4. Simpan hasil fungsi pada variabel check.
 5. Buatlah pengondisian dari variabel check dengan kriteria berikut.
    5.1. Apabila bernilai False, cetaklah teks "Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut."
    5.2. Apabila bernilai True, cetaklah teks "Rumah dapat dibangun berdasarkan ketiga nilai tersebut."
"""

# Tulis kode Anda di bawah ini
landArea:float = float(input("Masukkan Luas tanah : "))
width:float = float(input("Masukkan panjang tanah : "))
length:float = float(input("Masukkan lebar tanah : "))

def checkArea(landArea:float,width:float,length:float) ->bool:
    buildingArea:float = width * length
    if buildingArea > landArea:
        return False
    elif buildingArea <= landArea:
        return True
    check:bool = buildingArea
    return check

check:bool = checkArea(landArea,width,length)
if check == False:
    print("Rumah tidak dapat dibangun berdasarkan ketiga nilai tersebut.")
else:
    print("Rumah dapat dibangun berdasarkan ketiga nilai tersebut.")

print("\nQuiz 3 : Prosedur\n")

permission:int = int(input("Masukkan nilai(1 untuk True atau 0 untuk False )"))
city:str = str(input("Masukkan Kota : "))

def checkPermission(permission:int,city:str) -> None: #parameter
    if permission == 1:
        permission:bool = True
        print(f"Anda dapat membangun rumah di kota {city}.")
    elif permission == 0:
        permission:bool = False
        print(f"Anda tidak bisa membangun rumah di kota {city} karena berkas belum lengkap.")


checkPermission(permission,city) #argumen





