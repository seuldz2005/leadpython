main=0
import math
def cls(): print("\n" * 100)
while main==0:
	cls()
	print('Chương trình về câu lệnh lặp')
	print('1. Bài toán tính a!')
	print('2. Bài toán kiểm tra số nguyên tố')
	print('3. Bài làm bảng cửu chương')
	print('4. Sắp xếp mảng')
	print('5. Phương trình bậc 2')
	print('6. Đếm ngày ')
	main=int(input('Chọn chương trình: '))
	if main==1:
		cls()
		print('Bài toán tính số a!')
		print()
		s=1
		a=int(input('Nhập a: '))
		for i in range(1,a+1,1):
			s=s*i
		print(s)
		input()
	if main==2:
		cls()
		print('Bài toán kiểm tra số nguyên tố')
		print()
		dem=0
		a=int(input('Nhập A: '))
		for i in range(1,a+1):
			if (a%i==0): dem=dem+1
		if dem==2:
			print('Số', a ,'là số nguyên tố')
		else:
			print('Số', a ,'không phải là số nguyên tố')
		input()
	if main==3:
		cls()
		print('Bài làm bảng cửu chương')
		print()
		a=int(input('Nhập bảng cửu chương: '))
		for i in range(1,11):
			print(a,'x',i,'=',a*i)
		input()
	if main==4:
		cls()
		print('Sắp  xếp mảng')
		print()
		a = []
		n=int(input('Nhập số lượng phần tử của mảng: '))
		for i in range(1,n+1):
			a.append(int(input('Nhập số thứ %d: ' % (i))))
		for i in range(n-1):
			for j in range(i+1, n):
				if (a[i]>a[j]):
					temp=a[i]
					a[i]=a[j]
					a[j]=temp
		print(a)
		input()
	if main==5:
		cls()
		print('Phương trình bậc 2')
		print('ax^2+bx+c=0 (a!=0)')
		print()
		a=int(input('Nhập a: '))
		b=int(input('Nhập b: '))
		c=int(input('Nhập c: '))
		while a==0:
			print('Phương trình không phải là phương trình bậc 2')
			print('Mời bạn nhập lại a')
			a=int(input('Nhập a: '))
		if a!=0:
			denta=(b**2-4*a*c)
			if denta<0:
				x=(-b)/(2*a)
				print('Phương trình vô nghiệm:')
				print('x=',round(x,2))
			else:
				if denta==0:
					print('Phương trình có nghiệm kép:')
					print('x=',(-b)/(2*a))
				else:
					x1=((-b)+math.sqrt(denta))/(2*a)
					x2=((-b)-math.sqrt(denta))/(2*a)
					print('Phương trình có nghiệm')
					print('x1=',round(x1,2))
					print('x2=',round(x2,2))		
	if main==6:
		cls()
		print('Chương trình đếm ngày')		
		print('Bắt đầu từ:')
		d=int(input('Ngày: '))	
		m=int(input('Tháng: '))
		y=int(input('Năm: '))
		print('Đến ngày:')
		d2=int(input('Ngày: '))	
		m2=int(input('Tháng: '))
		y2=int(input('Năm: '))
		
	print('0. Trở về main')
	print('1. Thoát chương trình')	
	main=int(input('Chọn số: '))