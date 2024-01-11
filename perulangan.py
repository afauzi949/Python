for _ in range(5):
    print("Perintah ini berjalan sebanyak 5 kali.")
for i in range(5):
    print(f"Perintah ini mencetak angka {i}")

print("Dengan list/tuple")
for i in [0,"Bima", True, 97.5]:
    print(f"Perintah ini mencetak nilai {i}.")

print("\nDengan string")
for i in "Bima":
    print(f"Perintah ini mencetak karakter {i}.")

# eksekusi kondisi di awal 
iterasi = 0

while iterasi < 4:
    print(f"Perintah cetak angka {iterasi}")
    iterasi+= 1

# eksekusi kondisi di akhir 
iterateNumber = 0
iterateValue = True
while iterateValue:
    print(f"Perintah ini mencetak angka {iterateNumber}")
    iterateNumber = iterateNumber + 1
    if iterateNumber >= 5:
        iterateValue = False   

for i in range (1,6):
    for j in range (i):
        print("*", end = ' ')
    print("")


print("\nPenggunaan Break\n")
# Penggunaan Break
for i in range(1,6):
    print(f"Menaiki lantai {i}")
    if i == 4:
        print(f"Berhenti di lantai {i}")
        break
    print(f"Melewati lantai {i}")

print("\nPenggunaan Continue\n")
# penggunaan continue
for i in range(1,7):
    print(f"Menaiki lantai {i}")
    
    if i != 5:
        print(f"Melewati lantai {i}")
        continue

    print(f"Berhenti di lantai {i}")
    break

print("\nPenggunaan artimatika di perulangan\n")
# operasi aritmatika dalam perulangan
total = 0

for nilai in [4,5,8,10]:
    total += nilai
    print(f"Total sementara yaitu {total}")

print(f"Total Akhir adalah {total}")

# Quiz
"""
TODO:
 1. Buatlah variabel a bertipe data integer yang bernilai 1 untuk menyimpan nilai suku pertama.
 2. Buatlah variabel b bertipe data integer yang bernilai 2 untuk menyimpan nilai beda antar suku.
 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
 4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
    4.1. state i;
    4.2. menghitung suku ke-n berdasarkan state i dan simpan pada variabel Un; dan
    4.3. mencetak setiap variabel Un menggunakan perintah print dan parameter end.
 5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.
"""

# Barisan Aritmatika
a:int = 1
b:int = 2
n:int = int(input("Masukkan Suku yang ingin diketahui : "))

for i in range (1,n+1):
  Un:int = a + (i-1)*b
  print(f"{Un}",end =" ")

print()
"""
TODO:
 1. Buatlah variabel a bertipe data integer yang bernilai 4 untuk menyimpan nilai suku pertama.
 2. Buatlah variabel r bertipe data integer yang bernilai 3 untuk menyimpan nilai rasio antar suku.
 3. Buatlah perintah untuk meminta masukan pengguna yang bertipe data integer dan simpan pada variabel n sebagai nilai suku yang ingin diketahui.
 4. Lakukan perulangan mulai dari 1 hingga n+1 dengan
    4.1. state i;
    4.2. menghitung suku ke-n berdasarkan state i dan simpan pada variabel Un; dan
    4.3. mencetak setiap variabel Un menggunakan perintah print dan parameter end.
 5. Lakukan pemberhentian mencetak teks dengan perintah print tanpa isi.
"""

# Barisan Geometri
a:int = 4
r:int =3
n:int = int(input("Masukkan suku yang mau dicari : "))

for i in range(1,n+1):
    Un:int = a * r **(i-1)
    print(Un,end = " ")
