# Basics strings and integrers

# calling in terminal as day_2.my_x() or my_x() - depends of a way of importing it in terminal
# can't use 'return' dubble times
# functions you call with ()

def my_x():						#callin as my_x()
	print('Hello World')
	return("This is 'quote' inside")

def string_formating():
	print('Gose to moje ulubione piwo\nDobre jest!')
	print('Pils Czeski \t też dobry')

zz = 'Abrakadabra' 				#calling as zz

# universal commands:
# dir(zz)
# help(zz.upper)
# type(zz)
# len(zz)
# ord('T')

def str_yy():
	yy = 'Belgian Pale Ale'
	xx = 'Gose,IPA,APA,RIS'
	a = len(yy)
	b = yy[2]
	c = yy[3:7]
	d = yy[:-1]
	e = yy.find('P')
	f = yy.replace('Pale', 'Golden Strong')
	g = yy.split(' ')
	h = yy.upper()
	i = yy.lower()
	j = yy.capitalize()
	k = yy.isalpha()
	l = yy.rstrip()
	m = yy[::-1]          #reverse
	n = xx.split(',')
	return a,b,c,d,e,f,g,h,i,j,k,l,m,n

def int_yy():
	yy = 657
	xx = 4.132
	a = float(yy)
	b = int(xx)
	c = yy // xx
	d = yy / xx
	return a, b, c


