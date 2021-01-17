# Importing Internal & External
# pypi.org   --> 3 party library

import requests 				# 3 party library, using ex. requests.get()
# from requests import          using get()
# from requests import *		using get()
from day_7 import get_msg 		# internal
from datetime import datetime 	# external
import sys


xx = datetime.now()

def send(name, beer):
	msg = get_msg(my_name=name, my_beer=beer)
	return msg

r = requests.get('http://httpbin.org/json')

def print_json(rq):
	print(rq)

check_status_r = r.status_code

