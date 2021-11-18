a = int(input("Nilai a : "))
b = int(input("Nilai b : "))
c = int(input("Nilai c : "))
D = (b**2)-(4*a*c)
akar1 = (-b+(D**(0.5)))/2*a
akar2 = (-b-(D**(0.5)))/2*a
if D < 0:
	print("Fungsi tersebut tidak memiliki akar riil")
elif D > 0: 
	print("Akar akar dari persamaan tersebut adalah ", akar2, "dan", akar1)
else: 
	print("Fungsi tersebut memiliki akar kembar yaitu ", akar1)