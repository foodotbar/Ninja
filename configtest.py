#!/root/Desktop/workdir/python27/bin/python

import sys, os
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
    #print "cmd:" + cmd
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret = proc.communicate()[0].strip()
    if proc.returncode != 0:
        return 'ERROR'
    else:
        return ret


def execute(cmd='echo 0'):
    #print "cmd:" + cmd
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.communicate()[0].strip()


def now():
    return execute('date +%Y-%m-%d_%H:%M:%S')


def now2():
    return execute('date +%Y-%m-%d_%H-%M-%S')


def waitcmdfinish(cmdkeyword=["tar xzf", ".img.tar.gz"]):
    checkstr = "ps -ef| "
    for kw in cmdkeyword:
        checkstr = checkstr + "grep \"" + kw + "\"|"
    checkstr = checkstr + "grep -v grep"
    print "waiting:" + str(cmdkeyword)
    while execute(checkstr).strip() != '':
        time.sleep(5)

#waitcmdfinish()

def int2mask(mask_int):
    bin_arr = ['0' for i in range(32)]
    for i in range(mask_int):
        bin_arr[i] = '1'
    tmpmask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
    tmpmask = [str(int(tmpstr, 2)) for tmpstr in tmpmask]
    return '.'.join(tmpmask)

def createip(net="192.168.255.0/24", sn=1):
    base = net[0:net.find('/')]
    basearr = base.split('.')
    _sn = sn - 1
    return '.'.join([basearr[0], str(int(basearr[1])+_sn/256/254%256), str(int(basearr[2])+_sn/254%256), str(int(basearr[3])+_sn%254 +1)])

def createbc(net="192.168.255.0/24"):
    base = net[0:net.find('/')]
    basearr = base.split('.')
    a = 32 - int(net[net.find('/')+1:])
    if a<=8:
        return '.'.join([basearr[0],basearr[1],basearr[2], str(int(basearr[3])+(2**a-1))])
    elif a<=16:
        return '.'.join([basearr[0],basearr[1], str(int(basearr[2])+(2**(a-8)-1)),"255" ])
    else:
        return '.'.join([basearr[0],str(int(basearr[1])+(2**(a-16)-1)),"255","255" ])

def hostname(cmd="hostname -s"):
    return execute(cmd)

cf = ConfigParser.ConfigParser()
cf.read("config.ini")

#s = cf.sections()
#print s
vms = []
if not cf.has_section("autovms"):
    vms = cf.get("size", "vm").strip().split(',')
#print vms

PROFILE = "localtest"
if cf.has_option("common", "profile"):
    PROFILE = cf.get("common", "profile")
print "PROFILE: " + PROFILE

drives = []
if cf.has_option("size", "drive"):
    drivestr = cf.get("size", "drive")
    if len(drivestr) > 0:
        drives = drivestr.strip().split(',')
print "additional drives: " + str(drives)

nonecache = True
if cf.has_option("common", "nonecache"):
    nonecache = cf.get("common", "nonecache")

workdir = cf.get("common", "workdir") + '/'
print "workdir:" + workdir

hostpw = cf.get("common", "hostpw")

VMCORES = cf.get("size", "vmcores")
print "vmcores:" + VMCORES

VMMEM = cf.get("size", "vmmem")
print "vmmem:" + VMMEM

MAC_BASE = cf.get("common", "macbase")
print "macbase:" + MAC_BASE

ipnet = "192.168.1.0/24"
if cf.has_option("common", "ipnet"):
    ipnet = cf.get("common", "ipnet")
print "ipnet: " + ipnet

bridgeport = cf.get("common", "bridgeport")
print "bridgeport:" + bridgeport

qemuexec = cf.get("common", "qemuexec")
print "qemuexec:" + qemuexec

NETBROADCAST = createbc(ipnet)
NETBASE = ipnet[0:ipnet.find('/')]
NETMASK =  int2mask(int(ipnet[ipnet.find('/')+1:]))
if cf.has_option("common", "hostip"):
    HOSTIP = cf.get("common", "hostip")
else:
    HOSTIP = NETBROADCAST[:len(NETBROADCAST)-1] + "4"

print "HOSTIP:" + HOSTIP

workflow = []
relay = False
if cf.has_option("plan", "relay"):
    relay = cf.get("plan", "relay")
    workflow = cf.get("plan", "workflow").strip().split(',')

print "workflow:" + str(workflow)

VM = []
VM_IP = []
VM_loc = []
MAC_ADDR = []


nativedrive = False
if cf.has_option("common", "nativedrive"):
    nativedrive = cf.get("common", "nativedrive")

nativeprefix = ''
if cf.has_option("autovms", "nativeprefix"):
    nativeprefix = cf.get("autovms", "nativeprefix").replace("@@HOST", hostname())
    print "nativeprefix:" + nativeprefix

if cf.has_section("autovms"):
    num_VM = int(cf.get("autovms", "vmcount"))
    for i in range (0, int(num_VM)):
        vms.append(cf.get("autovms", "prefix") + str(i+1))
else:
    num_VM = len(vms)


for i in range(0, int(num_VM)):
    VM.append(vms[i])
    if cf.has_section("autovms"):
        VM_IP.append(createip(net=ipnet, sn=int(vms[i][2:])))
    else:
        VM_IP.append(cf.get(vms[i], "ip"))

    if cf.has_section("autovms"):
        VM_loc.append(cf.get("autovms", "locationprefix").replace("@@HOST", hostname())+str(i+1)+"/")
    else:
        VM_loc.append(cf.get(vms[i], "location"))

    MAC_ADDR.append(MAC_BASE + ("%02x"%(int(VM_IP[i].split('.')[1]))).upper() + ":" + ("%02x"%(int(VM_IP[i].split('.')[2]))).upper()
                    + ":" + ("%02x"%(int(VM_IP[i].split('.')[3]))).upper())

#if i<10 :
#	MAC_ADDR.append( MAC_BASE + "0" + str(i))
#else:
#	MAC_ADDR.append( MAC_BASE + str(i))



print "vms:" + str(VM)
print "ips:" + str(VM_IP)
print "location:" + str(VM_loc)
print "macs:" + str(MAC_ADDR)






