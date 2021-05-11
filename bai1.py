import math
print('Giải phương trình bậc nhất: ax+b=0')
a=float(input('nhap a '))
b=float(input('nhap b '))
if a==0:
	print('Vì a=0 nên không phải là phương trình bậc nhất')
elif a!=0:
	print('Phương trình có nghiệm:', -b/a)
	print()
input('Enter để kết thúc')