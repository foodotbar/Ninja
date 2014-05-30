#!/root/Desktop/workdir/python27/bin/python


import subprocess
import configtest

#make install qemu
#if configtest.qemuexec == 'qemu-system-x86_64':
#    configtest.execute0(
#        "mkdir -p /root/Desktop/iotest >/dev/null 2>&1; rm -rf /root/Desktop/iotest/qemu-1.5.3; tar xzf template/qemu-1.5.3.tar.gz -C /root/Desktop/iotest/")
#    configtest.execute0("cd /root/Desktop/iotest/qemu-1.5.3; make install; rm -rf /root/Desktop/iotest/qemu-1.5.3")



#generate the ifcfg-ethX brX

num_eth = configtest.bridgeport

if num_eth == 'dummy':
    print "Will add dummy0 to bridge local vm networks"
    configtest.execute0("modprobe dummy")
else:
    print "Will add port eth" + str(num_eth) + " to bridge local vm networks"

eth_temp_file = "template/ifcfg-eth_template"
br_temp_file = "template/ifcfg-br_template"

eth_file = "tmp/ifcfg-eth" + str(num_eth)
if num_eth == 'dummy':
    eth_file = "tmp/ifcfg-dummy0"

br_file = "tmp/ifcfg-br" + str(num_eth)
if num_eth == 'dummy':
    br_file = "tmp/ifcfg-brdummy0"

fp1 = open(eth_temp_file)
fp2 = open(eth_file, "w")
line = 'hello'
while (line != ''):
    #print line
    line = fp1.readline()
    if "DEVICE" in line:
        line = "DEVICE=eth" + str(num_eth)
        if num_eth == 'dummy':
            line = "DEVICE=dummy0"
        fp2.write(line + "\n")
    elif "BRIDGE" in line:
        line = "BRIDGE=br" + str(num_eth)
        if num_eth == 'dummy':
            line = "BRDIGE=brdummy0"
        fp2.write(line + "\n")
    else:
        fp2.write(line)
fp1.close()
fp2.close()

fp1 = open(br_temp_file)
fp2 = open(br_file, "w")
line = 'hello'
while (line != ''):
    #print line
    line = fp1.readline()
    if "DEVICE" in line:
        line = "DEVICE=br" + str(num_eth)
        if num_eth == 'dummy':
            line = "DEVICE=brdummy0"
        fp2.write(line + "\n")
    elif "@HOSTIP" in line:
        line = "IPADDR=" + configtest.HOSTIP
        fp2.write(line + "\n")
    elif "@HOSTNET" in line:
        line = "NETMASK=" + configtest.NETMASK
        fp2.write(line + "\n")
    else:
        fp2.write(line)
fp1.close()
fp2.close()
# copy the setting file to right path
cp_cmd = "/bin/cp " + eth_file + " " + br_file + " /etc/sysconfig/network-scripts/"
print cp_cmd
subprocess.call(cp_cmd, shell=True)

# restart the bridge and net interface
subprocess.call("service NetworkManager stop", shell=True)
subprocess.call("chkconfig NetworkManager off", shell=True)
subprocess.call("/sbin/service network restart", shell=True)

if num_eth == 'dummy':
    configtest.execute0("/usr/sbin/brctl addif brdummy0 dummy0")

#generate VMs list 
#num_hosts = 5

num_VM = configtest.num_VM
VM = configtest.VM
VM_IP = configtest.VM_IP
MAC_ADDR = configtest.MAC_ADDR

print num_VM
print VM
print VM_IP
print MAC_ADDR

#generate the /etc/hosts 
fp = open("/etc/hosts")
fp1 = open("tmp/hosts", 'w')
line = 'hello'
while (line != ''):
    print line
    line = fp.readline()
    if not "vm" in line:
        fp1.write(line)
for i in range(0, int(num_VM)):
    hostip = VM_IP[i]
    hostname = VM[i]
    fp1.write(hostip + '\t' + hostname + '\n')
    subprocess.call("mkdir /root/Desktop/workdir/result/" + hostname + " >/dev/null 2>&1", shell=True)
fp.close()
fp1.close()
cp_cmd = "/bin/cp tmp/hosts /etc/"
print cp_cmd
subprocess.call(cp_cmd, shell=True)

#generate VMs list and /etc/dhcp/dhcpd.conf
subprocess.call("pkill packagekitd; /usr/bin/yum install dhcp tunctl expect tcl tk tcl-devel tk-devel -y", shell=True)
fp = open("tmp/dhcpd.conf", 'w')
preCont = open("template/dhcpd_template.conf").readlines()
for line in preCont:
    if "@HOSTIP" in line:
        line = "option routers " + configtest.HOSTIP + ";\n"
        fp.write(line)
    elif "@HOSTBC" in line:
        line = "option broadcast-address " + configtest.NETBROADCAST + ";\n"
        fp.write(line)
    elif "@SUBNET" in line:
        line = "subnet " + configtest.NETBASE + " netmask " + configtest.NETMASK + " {\n"
        fp.write(line)
    else:
        fp.write(line)

for i in range(0, int(num_VM)):
    hostip = VM_IP[i]
    hostname = VM[i]

    host_setting = "host " + hostname + " { " + "\n" \
                   + "option host-name " + "\"" + hostname + "\";\n" \
                   + "hardware ethernet " + MAC_ADDR[i] + ";\n" \
                   + "fixed-address " + hostip + ";\n" \
                   + "}\n"

    #print host_setting
    fp.write(host_setting)
fp.write("}")
fp.close()

subprocess.call("/bin/cp tmp/dhcpd.conf /etc/dhcp/", shell=True)

subprocess.call(" /bin/sed -i 's/^DHCPDARGS.*//g' /etc/sysconfig/dhcpd", shell=True)
if num_eth == 'dummy':
    subprocess.call("cp template/qemu-ifup .; /bin/sed -i 's/@SWITCH/dummy0/g' ./qemu-ifup", shell=True)
else:
    subprocess.call("cp template/qemu-ifup .; /bin/sed -i 's/@SWITCH/" + num_eth + "/g' ./qemu-ifup", shell=True)
if num_eth == 'dummy':
    subprocess.call("echo 'DHCPDARGS=brdummy0' >> /etc/sysconfig/dhcpd", shell=True)
else:
    subprocess.call("echo 'DHCPDARGS=br" + str(num_eth) + "' >> /etc/sysconfig/dhcpd", shell=True)

subprocess.call("service dhcpd restart", shell=True)
