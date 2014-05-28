#!/usr/bin/python

import sys,os
import ConfigParser


cf = ConfigParser.ConfigParser()
cf.read("config.ini")

#s = cf.sections()
#print s

vms=cf.get("size","vm").strip().split(',')
#print vms


for vm in vms:
	print cf.get(vm, "ip")
	print cf.get(vm, "location")


