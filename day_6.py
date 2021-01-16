# string formating
# F-Strings
# .format
# f""
# \
# \n: New Line
# \t: Tab
# \\ or //: Allowed Slash
# \': Allowed Single Quote
# \": Allowed Double quote
# {{ or }}: Allowed single curly bracket in formatted strings
# "your single-line text": Wrap a single quote (') or double quote (") around text / numbers to make it a string.
#\: A slash in front of a return/enter will escape that. 


beer = 'Gose'
fav_beer = f'My fav beer is {beer}'   # it doeasn't work with triple """

beer_list = ['Gose', 'Berliner Weisse', 'Best Bitter']

def my_beers(my_list):
	for beer in my_list:
		print(f'my fav beer is {beer}')

template = '''My fav beer is {} but i also like {}'''
template2 = '''My fav beer is {beer} but i also like {beer2}'''
template3 = 'My fav beer is {beer} but i also like {}'.format('Gose', beer='Grodziskie')
template4 = 'My fav beer is {beer} but i also like {{}}'.format(beer='Grodziskie')
template5 = 'My fav beer is {0} but i also like {1}. But {0} is the best'.format('Gose', 'Duvel')
template6 = "My fav beer is {0} but i also like {1}. But {2[beer]} is the best".format('Gose', 'Duvel', {'beer':'Grodziskie APA'})
msg = template.format('Scotch Ale', 'NEIPA')
msg2 = template2.format(beer='Scotch Ale', beer2='NEIPA')

msg3 = "Hello my fav beer \
is of course Belgian Pale Ale"

my_pi = 4.14523413243524
msg4 = "{}".format(my_pi)
msg5 = "{:f}".format(my_pi)  #fraction
msg6 = "{:2f}".format(my_pi)

msg7 = format(my_pi, ".2f")

my_dict = {'beer':"Gose", 'type':'sour','price':"2 euro"}
msg8 = "My fav beer is {beer} which is {type}. \nThe price is {price}".format(**my_dict)

def get_msg8(msg):
	print(msg)

msg9 = "%s is my fav beer. But %s is also good" % ('Gose', 'American IPA')
msg10 = "%(beer)s is my fav beer. But %(beer2)s is also good" % {'beer':'Gose', 'beer2':'American IPA'}


