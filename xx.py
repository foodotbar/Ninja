#!/root/Desktop/workdir/python27/bin/python -u

import sys,os
import time
import ConfigParser
import subprocess


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def execute0(cmd='echo 0'):
    print "cmd:" + cmd
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    ret = proc.communicate()[0].strip()
    if proc.returncode != 0:
        return 'ERROR'
    else:
        return ret

def execute(cmd='echo 0'):
    #print "cmd:" + cmd
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE)
    return proc.communicate()[0].strip()

def waitcmdfinish(cmdkeyword=["tar xzf", ".img.tar.gz"]):
	checkstr = "ps -ef| "
	for kw in cmdkeyword:
		checkstr = checkstr + "grep \""+ kw +"\"|"
	checkstr = checkstr + "grep -v grep"
	print "waiting:" + str(cmdkeyword)
	while execute(checkstr).strip() != '':
		time.sleep(5)

#waitcmdfinish()


# print execute0("mkdir /root/Desktop/iotest >/dev/null 2>&1; rm -rf /root/Desktop/iotest/qemu-1.5.3; tar xzf qemu-1.5.3.tar.gz -C /root/Desktop/iotest/")
# print execute0("cd /root/Desktop/iotest/qemu-1.5.3; make install") 

for i in range(0,5):
	print "xx" + str(i)
	execute('sleep 5')


