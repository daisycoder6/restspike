"""
We won't drive the REST API with a browser.
We will build a library to drive the api 
"""

import requests

def checkserver():

	r = requests.get('http://localhost:8080/')

	return


def configure(payload):
	"""
	send arguments
	"""

	r = requests.get('http://localhost:8080/configure', params=payload)
	print(r.url)