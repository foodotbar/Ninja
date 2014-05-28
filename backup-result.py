#!/root/Desktop/workdir/python27/bin/python

import subprocess
import sys
import configtest


cmd = "cp config.ini result/ ;tar czf bak/result." + configtest.PROFILE + "." + configtest.now2() + ".tar.gz result"
print "exec: " + cmd
subprocess.call(cmd,shell=True)

for i in range(0,configtest.num_VM):
	cmd1 = "rm -f result/boot* result/*nmon result/*ini result/*info; rm -rf " + configtest.workdir + "result/"+configtest.VM[i]+"/*"
	print "exec: " + cmd1
	subprocess.call(cmd1,shell=True)

