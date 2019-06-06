#!/usr/bin/env python
#
#need function named devices
#need a list named routers
#need function named security
#need dictionary name credentials
#need function named combined
#need standard entry point

#my Functions
def devices(routers):
	print "The routers are:"
	print routers

def security(credentials):
	print "The credentials are:"
	print credentials

def combined():
	print "All data is"
	print routers
	print credentials

#My values
routers = ["router1","router2","router3"]
password = "passw0rd1"
credentials = {"router2":password,"router3":password,"router1":password}

#the Begining
if __name__ == '__main__':
	devices(routers)
	security(credentials)
	combined()