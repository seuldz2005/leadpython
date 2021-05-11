from tkinter import *
from tkinter.ttk import *
import tkinter
from playsound import playsound
import time

windows = Tk()
windows.title("Hello")
windows.geometry("600x200") #kích thước của cửa sổ
windows.configure(background = "pink")
windows.resizable(0, 0)
#hàm tăng giảm

h=00
m=00
s=00

#thêm tiêu đề:


lbl = tkinter.Label(windows, text=str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2), background = "pink", fg="BLACK", font=("Arial", 100))
lbl.grid(column=0, row=0)
i = 0
def uphh():
    global h, lbl 
    h = (h + 1)  
    txt = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    lbl['text'] = txt   

def dh():
    global h, lbl 
    if h>0:
    	h = (h - 1)  
    txt = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    lbl['text'] = txt 

def um():
    global m,h, lbl 
    m = (m + 1)  
    if m==60:
    	m=00
    	h=h+1
    txt = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    lbl['text'] = txt   

def dm():
    global m,h, lbl 
    if m>0:
    	m = (m - 1)  
    	if m==60:
    		m=00
    		h=h+1
    txt = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    lbl['text'] = txt 

def us():
    global s,m,h, lbl 
    s = (s + 1)  
    if s==60:
    	s=00
    	m=m+1
    	if m==60:
    		m=00
    		h=h+1
    txt = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    lbl['text'] = txt  

def ds():
    global s,m,h, lbl 
    if s>0:
    	s = (s - 1)  
    	if s==60:
    		s=00
    		m=m+1
    		if m==60:
    			m=00
    			h=h+1
    txt = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    lbl['text'] = txt 


#nhưng khi bấm nó lại không nhận
uph = tkinter.Button(windows, text="︿", fg="BLACK", font=("Arial", 20), command=uphh) #đoạn này thêm biến h vào biến để nó tính
uph.place(bordermode=OUTSIDE, height=20 , width=50, x=50, y=130)

downh = tkinter.Button(windows, text="﹀", fg="BLACK", font=("Arial", 20), command=dh)
downh.place(bordermode=INSIDE, height=20, width=50, x=50, y=155)

upm = tkinter.Button(windows, text="︿", fg="BLACK", font=("Arial", 20), command=um)
upm.place(bordermode=INSIDE, height=20, width=50, x=235, y=130)

downm = tkinter.Button(windows, text="﹀", fg="BLACK", font=("Arial", 20), command=dm)
downm.place(bordermode=INSIDE, height=20, width=50, x=235, y=155)

ups = tkinter.Button(windows, text="︿", fg="BLACK", font=("Arial", 20), command=us)
ups.place(bordermode=INSIDE, height=20, width=50, x=425, y=130)

downs = tkinter.Button(windows, text="﹀", fg="BLACK", font=("Arial", 20), command=ds)
downs.place(bordermode=INSIDE, height=20, width=50, x=425, y=155)

start = tkinter.Button(windows, text="▷", fg="BLACK", font=("Arial", 20), command=ds)
start.place(bordermode=INSIDE, height=30, width=50, x=530, y=40)

exit = tkinter.Button(windows, text="Close", fg="BLACK", font=("Arial", 20), command=exit)
exit.place(bordermode=INSIDE, height=30, width=80, x=500, y=140)

def clear():
	global h,m,s, lbl
	h=00
	s=00
	m=00
	lbl['text'] = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
def start():
	global h,m,s,lbl, start
	if start['text']=="■" and (h!=0 or m!=0 or s!=0):
		start['text']="▷"
		temp=-1
	if start['text']=="▷" and (h!=0 or m!=0 or s!=0):
		start['text']="■"
		temp=s
		while temp>-1:
			windows.update()
			if s>0: s-=1
			temp-=1
			time.sleep(1)
			if m>0 and s==0:
				m=m-1
				s=59
				temp=s
			elif h>0 and m==0:
				h=h-1
				m=59
				s=59
				temp=s
			lbl['text'] = str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
		start['text']="▷"
		playsound('ticktick.mp3')

start = tkinter.Button(windows, text="▷", fg="BLACK", font=("Arial", 20), command=start)
start.place(bordermode=INSIDE, height=30, width=50, x=530, y=40)

delete = tkinter.Button(windows, text="🗑", fg="BLACK", font=("Arial", 20), command=clear)
delete.place(bordermode=INSIDE, height=35, width=50, x=530, y=85)


windows.mainloop()

#Code By Seul
#1 days to finish
#Start to 23:00 10/5/2021 finish to 14:00 11/5/2021
#day_2 to lead python