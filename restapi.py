"""
Using bottlewe will define some resource locations.
This will allow us to exposefunctions within core
"""

from bottle import Bottle, run, get, post,static_file
from bottle import request, route, template, response
import core


@route('/')
#@view('topten')
def checkserver():

	core.print_status()
	return 

@route('/configure')
#@view('topten')
def get_config():

	args =request.query.getlist('args')
	print(args)

	core.configure_setup(args)
	return 


if __name__ == '__main__':

    run(host='localhost', port=8080,debug=True,reload=True)