try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()

config.read('config.ini')

#lấy thông tin từ config.ini
inputwithconfig=config.get('config_main','inputwithconfig')
if inputwithconfig=='true':
	a=config.getfloat('config_main','a')
	b=config.getfloat('config_main','b')
else:
	a=float(input('Nhập a: '))
	b=float(input('Nhập b: '))
lamtron=config.get('config_main','lamtron')
pheptinh=config.get('config_main','pheptinh')
lamtronden=config.getint('config_main','lamtronden')

#bắt đầu kiểm tra config và giải 
if pheptinh=='+':
	c=a+b
elif pheptinh=='-':
	c=a-b
elif pheptinh=='*':
	c=a*b
else:
	c=a/b
if lamtron=='true':
	slt=round(c,lamtronden)
else:
	slt=c
print(slt)

#lưu lại vào file result.txt
with open("result.txt",'a') as f:
	f.write(str(slt)+'\n')

#Code By Seul
#0:55 12/5/2021
#day_3 to lead python