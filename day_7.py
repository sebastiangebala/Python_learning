# Functions and Modules
# args kwargs
# lambda
# yield
# enumerate
# iter
# == / is
# keyword=None means that this keyword is not obligatory but you can fill it

msg_template = """ Hello {name}
I'm happy to informy that my fav beer is {beer}.
But don't worry, yours are also good!"""

def get_msg(my_name='Wietek', my_beer='Gose'):
	return msg_template.format(name=my_name, beer=my_beer)

beer_list = ['RIS', 'NEIPA', 'Grodziskie APA']
name_list = ['Adam', 'Bastek', 'Ola']

def get_meseg():
	for name in name_list:
		for beer in beer_list:
			print(msg_template.format(name=name, beer=beer))

def base_func(*args, **kwargs):
	print(args, kwargs)

# base_func('gose', 'wit', beer='NEIPA', kind='Fruity')

beer = 'Balgian Golden Strong Ale'

def beer_get(a, *b, c):   # hewe c is aa a keyword argument using --> beer_get('Gose', 'Flanders', c='Wit Beer')
	print(a,b,c)

beer2 = [('Gose', 'Berliner Weisse'), ('Lager', 'Ale'), ('sour', 'heavy')]
beer3 = [('Gose', 'Berliner Weisse', 'Baltic Porter'), ('Lager', 'Ale', 'Flanders'), ('sour', 'heavy', 'sweet')]

def unpack_list(my_list):
	for (item1, item2) in my_list:
		print(item1, item2) 			# return get only one iteration as a result

def unpack_list2(my_list):
	for (item1, *item2, item3) in my_list:
		print(item1, item2, item3)		# return get only one iteration as a result

def get_arg(*args):
	return args

def get_kwargs(**kwargs):
	return kwargs

def get_kwargs2(arg, **kwargs):
	return arg, kwargs

def get_lowest(*args):
	first = args[0]
	for num in args:
		if num < first:
			first = num
	return first

def my_func(n):
	return lambda a: a ** n

rand_var = my_func(5)

# using --> rand_var(23)

def my_func2(N):
	for i in range(N):
		yield i

gen = my_func2(55)

# using --> next(gen)

my_dict = {'beer':'Gose', 'type':'Sour', 'fav':'Duvel'}

aa = enumerate(my_dict)
bb = iter(my_dict)

# using --> next(aa), next(bb)

A = 'Wit Beer'
B = A
A = 'Gose'
# print(A, B)

#but!

C = ['Gose', 'Belgian Dubbel', 'Burton Ale']
D = C
C[1] = 'Czech Pils'
# print(C, D)

E = ['Gose', 'Belgian Dubbel', 'Burton Ale']
F = ['Gose', 'Belgian Dubbel', 'Burton Ale']
# print(E == F, E is F)

G = 'Porter'
H = 'Porter'
# print(G == H, G is H)