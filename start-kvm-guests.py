#!/root/Desktop/workdir/python27/bin/python -u

import subprocess
import sys
import time
import configtest
import os


## decompress image
overwrite = False

for ar in sys.argv[1:]:
    if ar.startswith("-o"):
        overwrite = True

for i in range(0, int(configtest.num_VM)):
#for i in range(0,1):
#       cmd = "dd if=" + configtest.workdir + "template/base.img" + " of=" + configtest.VM_loc[i] + configtest.VM[i] +".img"
    if overwrite or not os.path.isfile(configtest.VM_loc[i] + configtest.VM[i] + ".img"):
        cmd = "/bin/sh -c 'tar xzf " + configtest.workdir + "template/base.img.tar.gz -C " + configtest.VM_loc[
            i] + "&& mv -f " + configtest.VM_loc[i] + "base.img " + configtest.VM_loc[i] + configtest.VM[i] + ".img &'"
        print cmd
       # subprocess.call(cmd, shell=True)
    for ar in sys.argv[1:]:
        if ar.startswith("drive="):
            if overwrite or not os.path.isfile(configtest.VM_loc[i] + ar[6:] + ".img"):
                cmd1 = "tar xzf " + configtest.workdir + "template/" + ar[6:] + ".img.tar.gz -C " + configtest.VM_loc[
                    i] + " &"
                print cmd1
        #        subprocess.call(cmd1, shell=True)

configtest.waitcmdfinish()


## start kvm guests


def getboottime(guest='vm01'):
    booted = configtest.execute("curl http://" + guest + "/booted");
    uptime = configtest.execute("curl http://" + guest + "/uptime");
    if not configtest.is_number(booted):
        booted = 0
    if not configtest.is_number(uptime):
        uptime = 0
    return float(booted), float(uptime)


startbooting = int(round(time.time()))

bootstatus = []

cachestr = ".img,if=virtio,cache=none"

if configtest.nonecache == "false":
    cachestr = ".img,if=virtio"

for i in range(0, int(configtest.num_VM)):
    vmwhere = configtest.VM_loc[i]
    if configtest.nativedrive == "true":
        vmwhere = configtest.nativeprefix + str(i+1) +"/"
    bootstatus.append([startbooting, 0, 0])
    add_drive = ""
    for ar in sys.argv[1:]:
        if ar.startswith("drive="):
            add_drive = add_drive + " -drive file=" + vmwhere + ar[6:] + cachestr
    for dv in configtest.drives:
        add_drive = add_drive + " -drive file=" + vmwhere + dv + cachestr
    cmd = "nohup " + configtest.qemuexec + " --enable-kvm -m " + configtest.VMMEM + " -smp " + configtest.VMCORES \
      + " -drive file=" + vmwhere + configtest.VM[i] + cachestr \
      + add_drive \
      + " -vnc 0.0.0.0:" + str(i + 11) \
      + " -device e1000,netdev=net0,mac=" + configtest.MAC_ADDR[i] + " -netdev tap,id=net0," \
      + "script=" + configtest.workdir + "qemu-ifup >log/" + configtest.VM[i] + ".qemu.log &"
    print cmd
    subprocess.call(cmd, shell=True)
    #cmd1 = "echo "+ str(startbooting) + " > " + configtest.workdir+"result/"+configtest.VM[i]+"/"+ "booting"
    #print cmd1
    #subprocess.call(cmd1, shell=True)

print "Now probe booting:"


def allbooted():
    for bs in bootstatus:
        if bs[1] == 0 or bs[2] == 0:
            return False
    return True


status = False
while not status:
    for i in range(0, int(configtest.num_VM)):
        bt = getboottime(configtest.VM[i])
        bootstatus[i][1] = bt[0]
        bootstatus[i][2] = bt[1]
        if bt[1] != 0:
            print configtest.VM[i] + " boottime:" + str(bt[0] - bootstatus[i][0]) + " uptime:" + str(bt[1])
    time.sleep(10)
    status = allbooted()
print "All guests booted."

fp = open("result/boot." + configtest.hostname() +"." + configtest.PROFILE + "."+configtest.now() + ".txt", 'w')
fp.write("VM \t boottime \t uptime \n")
for i in range(0, int(configtest.num_VM)):
    fp.write(
        configtest.VM[i] + ' \t ' + str(bootstatus[i][1] - bootstatus[i][0]) + ' \t ' + str(bootstatus[i][2]) + '\n')
fp.close()


