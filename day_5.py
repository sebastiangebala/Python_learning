# conditionals and control flow
# True False
# While
# instance
# set
# math
# bin, oct, hex, evel
# round
# add
# Decimal, Fraction

import math as m
from decimal import Decimal
from fractions import Fraction


aa = not False
bb = 33 < 22 or 33 > 22
cc = 200 >= 200


abc = [1,2,3,4,5,6]

def sq_num(items):
	new_list = []
	for i in items:
		new_num = i**2
		new_list.append(new_num)
	return new_list

def get_even_and_odd(my_list):
	even = []
	odd = []
	for i in my_list:
		if i % 2 == 0:
			even.append(i)
		else:
			odd.append(i)
	print('this i even:', even, 'this is odd:', odd)

def looping(my_num1, my_num2):
	while my_num1 <= my_num2:
		print(my_num1)
		my_num1 += 1
	else:
		print(my_num1, ' is higher than ', my_num2)

random_list = ['aa', 123, 'koala', 344, 233, 'Gose', True, False]

def clean_list(some_list):
	list_num = []
	list_str = []
	list_ran = []
	for i in some_list:
		if isinstance(i, int):
			list_num.append(i)
		elif isinstance(i, str):
			list_str.append(i)
		else:
			list_ran.append(i)
	print(list_num, list_str, list_ran)


S1 = set('Kalambur')
S2 = set('Kamikadze')

S3 = S1 - S2
S4 = S1 ^ S2
# S5 = S1 + S2    use & insteed of +
S6 = S1 | S2
S7 = S1 & S2
S8 = S1.add('Koktajl')     #set can only contain str and int

A = m.floor(2.5)
B = m.floor(-2.5)
C = m.trunc(2.5)
D = m.trunc(-2.5)

Aa = bin(55)
Bb = oct(55)
Cc = hex(55)
Dd = eval(Aa)
Ee = round(34.2141352452, 3)

Ff = 0.1 + 0.1 + 0.1 - 0.3
Gg = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Hh = Fraction('0.25') + Fraction(2,3)
