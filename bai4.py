from tkinter import *
from tkinter.ttk import *
import tkinter

windows = Tk()
windows.title("Hello")
windows.geometry("1000x300") #kích thước của cửa sổ
windows.configure(background = "pink")
#thêm tiêu đề:


lbl = tkinter.Label(windows, text="Phép tính  A và B", background = "pink", fg="BLACK", font=("Arial", 30))
lbl.grid(column=0, row=0)

#thêm đối tượng

combo = Combobox(windows)
lblcombo = tkinter.Label(windows, text="Phép tính:",background = "pink", fg="BLACK", font=("Arial", 15))
lblcombo.grid(column=2, row=2)
combo['values'] = ("Tính Tổng", "Tính Hiệu", "Tính Tích", "Tính Thương", "Hàm bậc nhất: ax+b=0")
combo.current(0)
combo.grid(column=3, row=2)

txta = Entry(windows, width=15)
txta.grid(column=2, row=3)

lbla = tkinter.Label(windows, text="Nhập A:",background = "yellow", fg="BLACK", font=("Arial", 15))
lbla.grid(column=1, row=3)

txtb = Entry(windows, width=15)
txtb.grid(column=4, row=3)

lblb = tkinter.Label(windows, text="Nhập B:",background = "yellow", fg="BLACK", font=("Arial", 15))
lblb.grid(column=3, row=3)

output = tkinter.Label(windows, text="Kết quả: ",background = "red", fg="BLACK", font=("Arial", 20))
output.grid(column=3, row=6)

def handleButton():
	pheptinh=str(combo.get())
	if pheptinh=="Tính Tổng":
		a=int(txta.get())
		b=int(txtb.get())
		c=a+b
		print(c)
	if pheptinh=="Tính Hiệu":
		a=int(txta.get())
		b=int(txtb.get())
		c=a-b
	if pheptinh=="Tính Tích":
		a=int(txta.get())
		b=int(txtb.get())
		c=a*b
	if pheptinh=="Tính Thương":
		a=int(txta.get())
		b=int(txtb.get())
		if b==0:
			c="PTVN"
		else:
			c=round(a/b, 2)
	if pheptinh=="Hàm bậc nhất: ax+b=0":
		a=int(txta.get())
		b=int(txtb.get())
		if a==0:
			c="PTVN"
		else:
			c=round(-b/a, 2)
	output['text'] = "Kết quả: " + str(c)		
#thêm nút

btnHello = tkinter.Button(windows, text="TÍNH", fg="BLACK", font=("Arial", 20), command=handleButton)
btnHello.grid(column=3, row=4)

 
windows.mainloop()

#in ra kết quả
