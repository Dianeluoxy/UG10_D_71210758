makanan = int(input("Harga makanan sebesar Rp "))
snack = int(input("Harga snack sebesar Rp "))
minuman = int(input("Harga minuman sebesar Rp "))
uang = int(input("Uang yang anda bawa sebesar Rp "))

total = makanan + snack + minuman
print("\nTotal yang harus anda bayar sebesar Rp", total)

if total > uang:
	print("Uang Anda kurang! Anda memiliki utang sebesar Rp", total-uang)
elif total == uang:
	print("Uang anda pas! Tidak ada kembalian dan Utang :D")
else:
	print("Anda memiliki kembalian sebesar Rp", uang-total)