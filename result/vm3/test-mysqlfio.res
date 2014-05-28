mysql-binlog: (g=0): rw=write, bs=512-1K/512-1K/512-1K, ioengine=sync, iodepth=1
...
mysql-binlog: (g=0): rw=write, bs=512-1K/512-1K/512-1K, ioengine=sync, iodepth=1
innodb-data: (g=0): rw=randrw, bs=16K-16K/16K-16K/16K-16K, ioengine=psync, iodepth=1
...
innodb-data: (g=0): rw=randrw, bs=16K-16K/16K-16K/16K-16K, ioengine=psync, iodepth=1
innodb-trxlog: (g=0): rw=write, bs=512-2K/512-2K/512-2K, ioengine=sync, iodepth=1
...
innodb-trxlog: (g=0): rw=write, bs=512-2K/512-2K/512-2K, ioengine=sync, iodepth=1
fio-2.0.13
Starting 160 processes
mysql-binlog: Laying out IO file(s) (1 file(s) / 500MB)
innodb-data: Laying out IO file(s) (1 file(s) / 1024MB)
innodb-trxlog: Laying out IO file(s) (1 file(s) / 300MB)

mysql-binlog: (groupid=0, jobs=160): err= 0: pid=2930: Tue Jan  7 16:55:47 2014
  read : io=150928KB, bw=514874 B/s, iops=31 , runt=300171msec
    clat (msec): min=3 , max=19134 , avg=806.62, stdev=1056.99
     lat (msec): min=3 , max=19134 , avg=806.62, stdev=1056.99
    clat percentiles (msec):
     |  1.00th=[   37],  5.00th=[   88], 10.00th=[  196], 20.00th=[  314],
     | 30.00th=[  412], 40.00th=[  515], 50.00th=[  635], 60.00th=[  783],
     | 70.00th=[  938], 80.00th=[ 1123], 90.00th=[ 1385], 95.00th=[ 1631],
     | 99.00th=[ 2868], 99.50th=[ 8356], 99.90th=[15401], 99.95th=[16319],
     | 99.99th=[16712]
    bw (KB/s)  : min=    0, max=   93, per=4.60%, avg=23.10, stdev=13.29
  write: io=41799KB, bw=142576 B/s, iops=19 , runt=300205msec
    clat (usec): min=4 , max=28883K, avg=3598675.91, stdev=4756927.18
     lat (usec): min=4 , max=28883K, avg=3598676.52, stdev=4756927.18
    clat percentiles (usec):
     |  1.00th=[    5],  5.00th=[   10], 10.00th=[   14], 20.00th=[177152],
     | 30.00th=[432128], 40.00th=[757760], 50.00th=[1155072], 60.00th=[2670592],
     | 70.00th=[4947968], 80.00th=[7897088], 90.00th=[9633792], 95.00th=[10944512],
     | 99.00th=[16711680], 99.50th=[16711680], 99.90th=[16711680], 99.95th=[16711680],
     | 99.99th=[16711680]
    bw (KB/s)  : min=    0, max=   93, per=5.53%, avg= 7.69, stdev=11.26
    lat (usec) : 10=1.87%, 20=2.70%, 50=0.87%, 100=0.07%, 750=0.02%
    lat (usec) : 1000=0.03%
    lat (msec) : 2=0.02%, 4=0.02%, 10=0.05%, 20=0.22%, 50=1.30%
    lat (msec) : 100=3.08%, 250=6.98%, 500=18.88%, 750=14.67%, 1000=12.40%
    lat (msec) : 2000=18.75%, >=2000=18.07%
  cpu          : usr=0.00%, sys=0.00%, ctx=45577, majf=0, minf=4608
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=9433/w=5950/d=0, short=r=0/w=0/d=0

Run status group 0 (all jobs):
   READ: io=150928KB, aggrb=502KB/s, minb=502KB/s, maxb=502KB/s, mint=300171msec, maxt=300171msec
  WRITE: io=41799KB, aggrb=139KB/s, minb=139KB/s, maxb=139KB/s, mint=300205msec, maxt=300205msec

Disk stats (read/write):
    dm-0: ios=9435/13239, merge=0/0, ticks=1168582/1350473, in_queue=2519122, util=100.00%, aggrios=9460/12383, aggrmerge=0/1852, aggrticks=1169326/1117057, aggrin_queue=2286366, aggrutil=100.00%
  vda: ios=9460/12383, merge=0/1852, ticks=1169326/1117057, in_queue=2286366, util=100.00%
