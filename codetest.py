try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()

config.read('config.ini')

a=ConfigParser.getfloat(config,a)
b=ConfigParser.getfloat(config,b)
lamtron=ConfigParser.getboolean(config,lamtron)
pheptinh=ConfigParser.get(config,pheptinh)
lamtronden=ConfigParser.getint(config,lamtronden)

if pheptinh=="+":
	c=a+b
elif pheptinh=="-":
	c=a-b
elif pheptinh=="*":
	c=a*b
else:
	c=a/b
if lamtron=="true":
	print(round(c,lamtronden))
else:
	print(c)