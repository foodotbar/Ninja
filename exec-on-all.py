#!/root/Desktop/workdir/python27/bin/python

import subprocess
import sys
import configtest

if len(sys.argv)<2 :
	print "pls give a executable cmd!"
	sys.exit()


for cmd in sys.argv[1:] :
	print "Executing: " + cmd
	for i in range(0, configtest.num_VM):
		print "At " + configtest.VM[i] + " :"
		print configtest.execute("ssh root@"+configtest.VM[i] + " '" + cmd + " '")


