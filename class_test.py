#class in python

class hocsinh:
	def __init__(self, ten, ngaysinh, sdt):
		self.ten = ten
		self.ngaysinh = ngaysinh
		self.sdt = sdt
	def inthongtin(self):
		print("Tên: "+ self.ten)
		print("Ngày Sinh: "+self.ngaysinh)
		print("Số điện thoại: "+self.sdt)


a = input('Nhập tên học sinh: ')
b = input('Nhập SĐT: ')
c= input('Nhập ngày Sinh: ')
hocsinha = hocsinh(a, b, c)


hocsinha.inthongtin()
