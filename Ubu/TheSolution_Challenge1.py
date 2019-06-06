#!/usr/bin/env python
#
#need function named devices
#need a list named routers
#need function named security
#need dictionary name credentials
#need function named combined
#need standard entry point

#my Functions
def devices():
	routers = ["router1","router2","router3"]
	print routers

def security():
	password = "passw0rd1"
	credentials = {"router1":password,"router2":password,"router3":password}
	print credentials

def combined():
	devices()
	security()

#the Begining
if __name__ == '__main__':
	print "The routers are:"
	devices()
	print "The credentials are"
	security()
	print "All data is"
	combined()