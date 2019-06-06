switch = "Juniper EX2200"
if "Catalyst" in switch:
	print "This is a Catalyst Switch"
elif "Nexus" in switch:
	print "This is a Nexus Switch"
elif "CatOS" in switch:
	print "This is an old CatOS. Prepare to upgrade"
else:
	print "This device is non-Cisco"