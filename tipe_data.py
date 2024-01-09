a = 5
b = 10.5
c = "anjay"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# deklarasi list number
angka = [10,20,5,7]
print(angka)

# mengakses elemen berdasarkan index
print(angka[0])
print(angka[3])

# mengubah nilai elemen indeks ke-1 
angka[0] = 980
print(angka[0])

# menambahkan elemen di indeks ke-2
angka.insert(1,9)
print(angka)

# menghapus elemen di indeks ke-2
angka.pop(1)
print(angka)

# deklarasi variabel list
print("\nList dengan tipe data berbeda")

mylist = [1,2.5,True,"Anjay",["sub1","sub2"]]
print(mylist)

# akses elemen index ke-3
print(mylist[2]) 

# akses elemen dalam sublist
print(mylist[4][0])

# deklarasi variabel tuple
print("\nTipe data Tuple (immutable)")
mytuple = (10,13,45,99)
print(mytuple)

# akses elemen index ke-4
print(mytuple[3])

# deklarasi variabel set a dan b
print("\nTipe data set (unik dan tidak urut)")
a = {10,15,20}
b = {15,25,30}

# operasi gabungan
gabungan = a.union(b)
print(f"gabungan a dan b adalah {gabungan}")

# operasi irisan
irisan = a.intersection(b)
print(f"irisan a dan b adalah {irisan}")

# operasi perbedaan
perbedaan = a.difference(b)
print(f"Pebedaan a dan b adalah {perbedaan}")

# deklarasi variabel dictionary
print("\nTipe data Dictionary (key-value & mutable pada value)")
propertidetail = {
    "lantai" : 1,
    "properti" : "rumah",
    "hasterace" : True,
    "hasgarage" : False
}
print(propertidetail)

# akses elemen dalam dictionary
print(propertidetail["properti"])
print(f"Punya teras ? {propertidetail['hasterace']}")

# mengubah nilai/value pada dictionary
propertidetail["properti"] = "hotel"
print(propertidetail)
print(propertidetail["properti"])

# Anotasi variabel
name : str = "bima"
age : int = 17

# Tipe data primitif
hasteras:bool = True
area:float = 9.5

# Tipe data non-Primitif
angka:list = [10,22,34,2]
buah:tuple = ("mangga","jeruk","apel")
warna:set = {"kuning","hijau","biru"}
supermarket:dict = {
    "nama" : "apel",
    "kode" : 2,
    "matang" : True
}

# Tipe data non-Primitif Spesifik
angkalist: list[int] = [10,22,33,76]
buahtuple: tuple[str] = ("mangga","apel")
colorset: set[str] = {"kuning","hijau"}
detaildictionary: dict[str,any] = {
    "nama" : "apel",
    "kode" : 2,
    "matang" : True
}

# tipe data non-primitif multi tipe data
numbersList: list[int, float] = [23, 52.3, 34]
fruitsTuple: tuple[str, int, bool] = ("Apel", "Jeruk", 10, True)
colorSet: set[int, str] = {225, "Biru", "Merah"}
propertyDetailDict: dict[str, tuple[int, str]] = {
    "numFloors": 1,
    "propertyType": "Rumah",
    "hasTerrace": True,
    "hasGarage": False
}
