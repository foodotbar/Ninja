Ninja
=====

a storage testing framework for data center via run test scripts in VMs

1. get and compile Python 2.7 under /root/Desktop/workdir/
2. download base.img.tar, disk-0.img.tar, qemu-1.5.3.tar from http://pan.baidu.com/s/1hqf11v2 to /root/Desktop/workdir/template/
3. edit the config.ini file, set your Host-Node's password, and the place where your VM's disk images
4. then run ./gethostready.py, get your host ready for VMs to start
5. then run ./startVMs.py, start the test VMs, when all VMs get start, you can get a file under /root/Desktop/work/result/ named boot.XXX…… contains VMs' start time and up time
6. then run ./nokeyssh.py, then make VMs and Host ssh each other via no-password
7. then run ./getresult.py, scp all the test scripts under /root/Desktop/workdir/script/ to each VM, and run, then get the results, scp back to Host, the results keep under /root/Desktop/workdir/result/xxVM/ folder
8. then run ./getreport, the parse program will get csv report for you, report keeps under /root/Desktop/workdir/report/
9. now, attention, you should run ./reset-boot-time.sh to make sure the next time, you can get the VM's right start time
10. Okay, finally you should halt all the VM, just run ./exec-on-all.py halt
11. If you have any questions, ask me

I used this framework testd Gluster, NFS, iSCSI, ceph, Sheepdog, local HDD, local SSD, their Read/Write rate and IOPS and bandwith.

a typical report like this:

https://github.com/foodotbar/Ninja/blob/master/report/details.2vms.2014-02-18_20_42_33.csv

and this:



https://github.com/foodotbar/Ninja/blob/master/report/fiotests.2vms.2014-02-20_22_15_58.csv
