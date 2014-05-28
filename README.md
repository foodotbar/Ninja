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

I used this framework testd Gluster, NFS, iSCSI, ceph, Sheepdog, local HDD, local SSD, their Read/Write rate and IOPS and bandwith.

a typical report like this:

testHostname	profile	vmName	BootTime(second)	UpTime(second)	dd-ndw(MB/s)	dd-dw(MB/s)	dd-ndr(MB/s)	dd-dr(MB/s)	MYSQL-R-ipos	MYSQL-W-ipos	Video-Write	Video-Random-R	Viedo-Stride-R
hcg1	gluster-4nodes-1	vm1	-178377	16.4	52.2	53.3	61	56	182	49	51539	3311342	3743341
hcg1	gluster-4nodes-1	vm2	36	31.04	51	50.1	80	53	181	48	44125	3580267	3306130


vm1	read iops=	84	write iops=	40					
750(usec)	1000(usec)	2(msec)	4(msec)	10(msec)	20(msec)	50(msec)	100(msec)	250(msec)	500(msec)
0.05%,	0.25%	32.19%,	6.55%,	32.66%,	21.18%,	6.87%	0.24%,	0.02%,	0.01%
vm1	write iops=	100							
750(usec)	1000(usec)	2(msec)	4(msec)	10(msec)	20(msec)				
0.15%,	0.17%	99.28%,	0.35%,	0.03%,	0.02%				
vm1	read iops=	100							
750(usec)	1000(usec)	2(msec)	4(msec)	10(msec)	20(msec)	50(msec)			
0.18%,	7.40%	91.08%,	0.47%,	0.53%,	0.30%,	0.03%			
vm2	read iops=	84	write iops=	41					
750(usec)	1000(usec)	2(msec)	4(msec)	10(msec)	20(msec)	50(msec)	100(msec)	250(msec)	
0.03%,	0.08%	32.77%,	6.48%,	32.83%,	20.74%,	6.83%	0.24%,	0.01%	
vm2	write iops=	100							
750(usec)	1000(usec)	2(msec)	4(msec)	10(msec)	50(msec)				
0.10%,	0.55%	99.08%,	0.20%,	0.05%,	0.02%				
vm2	read iops=	100							
750(usec)	1000(usec)	2(msec)	4(msec)	10(msec)	20(msec)	50(msec)			
0.72%,	18.28%	79.95%,	0.38%,	0.43%,	0.22%,	0.02%			
