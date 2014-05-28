#!/root/Desktop/workdir/python27/bin/python -u

import subprocess
import os, fnmatch, time
import configtest


def proberesult(targetdir=configtest.workdir + "/result", subdirpattern="vm*", resultsuffix=".tar.gz"):
    ct = len(configtest.VM)
    subdirs = os.listdir(targetdir)
    count = 0
    finishcount = 0
    for subdir in subdirs:
        if fnmatch.fnmatch(subdir, subdirpattern):
            count += 1
            if len(filter(lambda x: x.endswith(resultsuffix), os.listdir(targetdir + "/" + subdir))) > 0:
                finishcount += 1
    return ct, finishcount


cmd1 = "rm -f tmp/script.tar.gz; tar czf " + configtest.workdir + "/tmp/script.tar.gz -C " + configtest.workdir + " script/"
print "exec: " + cmd1
subprocess.call(cmd1, shell=True)

configtest.execute("script/hw-info.sh > result/host-hw.info")

for i in range(0, configtest.num_VM):
    cmd2 = "scp " + configtest.workdir + "/tmp/script.tar.gz " + "root@" + configtest.VM_IP[i] + ":/root/"
    print "exec: " + cmd2
    subprocess.call(cmd2, shell=True)

    cmd5 = "ssh root@" + configtest.VM_IP[i] + " rm -rf script"
    print "exec: " + cmd5
    subprocess.call(cmd5, shell=True)

    cmd3 = "ssh root@" + configtest.VM_IP[i] + " tar xzf " + "script.tar.gz"
    print "exec: " + cmd3
    subprocess.call(cmd3, shell=True)

if not configtest.relay:

    print "Put all scripts to test, no relay"

    for i in range(0, configtest.num_VM):
        cmd4 = "ssh root@" + configtest.VM_IP[
            i] + " '/bin/sh -c \"(nohup ./script/run-tests.sh) > ./script/run-tests.log &\"'"
        print "exec: " + cmd4
        subprocess.call(cmd4, shell=True)

    cmd6 = "pkill nmon;./nmon -F result/host." + configtest.now() + ".nmon -s5"
    print "exec: " + cmd6
    subprocess.call(cmd6, shell=True)

    status = proberesult()
    print status
    pdelta = status[0] - status[1]
    print "Waiting " + str(pdelta) + " more result(s).."
    while status[0] != status[1]:
        if pdelta != status[0] - status[1]:
            print "Waiting " + str(status[0] - status[1]) + " more result(s).."
            pdelta = status[0] - status[1]
        time.sleep(10)
        status = proberesult()

    cmd6 = "pkill nmon"
    print "exec: " + cmd6
    subprocess.call(cmd6, shell=True)
    print "Test in guests finished, pls check result dir."

else:
    # relay to workflow
    #cmd6 = "pkill nmon;./nmon -F result/host." + configtest.now() + ".nmon -s5"
    #print "exec: " + cmd6
    #subprocess.call(cmd6, shell=True)

    for teststep in configtest.workflow:
        print "Now running: " + teststep
        configtest.execute("pkill nmon;./nmon -F result/" + configtest.hostname() +"." + configtest.PROFILE+"." + str(len(configtest.VM)) + "vms." +
                           teststep+"."+ configtest.now() + ".nmon -s5")
        for i in range(0, configtest.num_VM):
            configtest.execute(
                "ssh root@" + configtest.VM_IP[i] + " '/bin/sh -c \"(nohup ./script/run-single-test.sh " +
                teststep + ") > ./script/run-single-test." + teststep + ".log &\"'")

        status = proberesult(resultsuffix=teststep + ".tar.gz")
        print status
        pdelta = status[0] - status[1]
        print "Waiting " + str(pdelta) + " more results for:" + teststep
        while status[0] != status[1]:
            if pdelta != status[0] - status[1]:
                pdelta = status[0] - status[1]
            time.sleep(10)
            status = proberesult(resultsuffix=teststep + ".tar.gz")
        print teststep + " finished."

    #cmd6 = "pkill nmon"
    #print "exec: " + cmd6
    #subprocess.call(cmd6, shell=True)
    print "All test in guests finished, pls check result dir."





