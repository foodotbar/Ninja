Ninja
=====

a storage testing framework for data center via run test scripts in VMs

1. get and compile Python 2.7 under /root/Desktop/workdir/
2. download base.img.tar, disk-0.img.tar, qemu-1.5.3.tar from pan.baidu.com/xxxxx to /root/Desktop/workdir/template/
3. edit the config.ini file, set your Host-Node's password, and the place where your VM's disk images
4. then run ./prepare-host.py, get your host ready for VMs to start
5. then run ./start-kvm-guests.py, start the test VMs, when all VMs get start, you can get a file under /root/Desktop/work/result/ named boot.XXX…… contains VMs' start time and up time
6. then run ./ssh-nokey.py, then make VMs and Host ssh each other via no-password
7. then run ./kickout-test.py, scp all the test scripts under /root/Desktop/workdir/script/ to each VM, and run, then get the results, scp back to Host, the results keep under /root/Desktop/workdir/result/xxVM/ folder
8. then run ./getreport, the parse program will get csv report for you, report keeps under /root/Desktop/workdir/report/
9. now, attention, you should run ./reset-boot-time.sh to make sure the next time, you can get the VM's right start time
10. Okay, finally you should halt all the VM, just run ./exec-on-all.py halt
11. If you have any questions, ask me

I used this test framework testd Gluster, NFS, iSCSI, ceph, Sheepdog, local HDD, local SSD, their Read/Write rate and IOPS and bandwith.
