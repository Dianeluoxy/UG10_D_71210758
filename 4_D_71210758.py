bil1 = int(input("Masukkan bilangan 1 : "))
bil2 = int(input("Masukkan bilangan 2 : "))
bil3 = int(input("Masukkan bilangan 3 : "))
kal = str("Urutan bilangan dari yang terbesar adalah")
if bil1>bil2:
	if bil2>bil3:
		print(kal, bil1, bil2, bil3)
	else: 
		print(kal, bil1, bil3, bil2)
elif bil2>bil3:
	if bil3>bil1:
		print(kal, bil2, bil3, bil1)
	else:
		print(kal, bil2, bil1, bil3)
else:
	if bil1>bil2:
		print(kal, bil3, bil1, bil2)
	else:
		print(kal, bil3, bil2, bil1)
	
