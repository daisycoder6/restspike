"""
Some core function definitions to emulate the application code
"""

import time
start_time = time.time()

import pandas
import numpy
import scipy
import matplotlib



def configure_setup(args):
	"""
	configure settings
	"""

	print(args)



def print_status():
	"""
	Print something to show connection
	"""

	print('Server up and running')

def main():


	payload = {"args": ["leo", "lo"]}

	print_status()
	configure_setup(payload['args'])

if __name__ == '__main__':

	main()
	print("--- %s seconds ---" % (time.time() - start_time))
