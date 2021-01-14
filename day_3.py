# Lists and dictionaires

def my_list():
	beer = ['Pale Ale', 'Gose', 'Berliner Weisse', 'Golden', 'Porter']  #position in the list in unchenged
	a = beer.append('Flanders')
	beer[2] = 'Gotlandsdrickke'     #the list is changing
	b = len(beer)
	c = beer[0]
	d = beer.reverse()
	e = beer.pop(3)
	f = beer.remove('Gose')
	beer2 = beer + ['NEIPA', 'American Pumpkin Ale', 'Wee Heavy']
	h = beer2.sort()
	i = beer2.extend(['Grodziskie', 'RIS'])
	j = beer2.index('NEIPA')
	return beer,a,b,c,d,e,f,beer2,h,i,j

def my_matrix():
	Mat = [[232, 554, 82],
			['Alicja', 'Iza', 'Renata'],
			[True, False,True]]
	a = Mat[1]
	b = Mat[1][2]
	c = [i[1] for i in Mat]
	d = [[Mat[i][j] for i in [0,1,2]] for j in [0,1,2]]
	e = [Mat[i][i] for i in [0,1,2]]
	return a,b,c,d,e

def result_generator():
	M = [[32,34,23], [45,34,56], [67,99,12]]
	a = (sum(row) for row in M)
	return next(a)

def my_map():
	M = [[32,34,23], [45,34,56], [67,99,12]]
	a = list(map(sum, M))
	return a

def my_dict():
	beers = {'Belgian':'Belgian Pale Ale', 'German':'Gose', 'American':'NEIPA'}   #no position
	a = beers['Belgian']
	b = beers.keys()
	c = beers.values()
	d = list(beers.values())
	e = list(beers.values())[1]
	beers['Polish'] = 'Baltic Porter'
	f = {ord(i) for i in 'Brewery'}
	g = beers.items()
	h = beers.pop('German')             # it works differ in lists -> by position
	beers2 = {'Beer':{'sour':'Gose', 'sweet':'Wee Heavy', 'heavy':'RIS'}, 'Price':[8,19,16]}
	i = (beers2['Beer']['sour'], beers2['Price'][0])
	return a,b,c,d,e,beers,f,g,h,i