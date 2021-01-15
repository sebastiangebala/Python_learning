# iteration and loops
# sorted function
# random
# range

from random import random, randint, choice

beer = ['Gose', 'Balgian Pale Ale', 'Wee Heavy', 'American IPA', 'Berliner Weisse']
beer2 = ['Gose', 'Belgian Golden', 'Scotch Ale', 'American IPA']
list_of_beers = [{'Type':'Gose', 'Example':'bee1'},{'Type':'English IPA', 'Example':'bee2'},
{'Type':'Belgian IPA', 'Example':'bee3'},{'Type':'Scotch Ale', 'Example':'bee4'}]

my_dict = {}
my_dict['Beer'] = 'Duvel'
my_dict['Type'] = 'Belgian Golden Stong Ale'
my_dict['Price'] = '4 euro'

def list_of_smth(some_list):
	for i in some_list:
		print(i)

def list_of_nums(x, y):
	for i in range(x, y):
		print(i)

def list_from_dict_vals(key, my_list):
	for i in my_list:
		print(i[key])

def find_beer(beer_name, my_list):
	for i in my_list:
		if 'Type' in i:
			if i['Type'] == beer_name:
				print(i)


def sort_info(my_dict):
	for i in sorted(my_dict):
		print(i, my_dict[i])


aa = randint(1, 100)
bb = random()
cc = choice(beer2)



def show_pairs(some_dict):
	for i in some_dict:
		print(i, ' --> ', some_dict[i])


def compare_lists(list1, list2):
	for i in list1:
		if i in list2:
			print(i, 'included')
		else:
			print(i, 'excluded')

ss = list(range(5))
ss1 = list(range(2,8))
ss2 = list(range(2,50,4))



