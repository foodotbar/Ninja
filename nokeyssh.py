#!/root/Desktop/workdir/python27/bin/python

import subprocess
import sys
import configtest

subprocess.call("cp template/ssh-nokey.sh .; /bin/sed -i 's/@HOSTPW/" + configtest.hostpw  +"/g' ./ssh-nokey.sh",shell=True)

# read VM list from .cfg file
#subprocess.call(configtest.workdir + "/keygen.sh",shell=True)

subprocess.call("rm -f /root/.ssh/*;/usr/bin/ssh-keygen -t rsa -N \"\" -f /root/.ssh/id_rsa", shell=True)

for i in range(0,configtest.num_VM):
	cmd = configtest.workdir + "ssh-nokey.sh " + configtest.VM[i]
	print cmd
	subprocess.call(cmd, shell=True)
 

subprocess.call("/usr/bin/ssh-add")