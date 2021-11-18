daftar1 = input("Masukkan daftar belanja Anda : ")
list1 = daftar1.title()
list2 = list1.split(", ")

print("Daftar belanja : ", list2)
daftar2 = (input("Masukkan barang yang ingin ditambahkan : "))

if (daftar2.title() in list2) == True: 
	print("Barang", daftar2.upper(), "sudah berada dalam daftar belanja.")
else: 
	#tambahbarang = list2 += _daftar2
	_daftar2 = daftar2.upper()
	list2.append(_daftar2)
	print("Hasil penambahan pada daftar belanja : ", list2)