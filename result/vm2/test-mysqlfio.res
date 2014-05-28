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

mysql-binlog: (groupid=0, jobs=160): err= 0: pid=2898: Tue Jan  7 16:54:26 2014
  read : io=115776KB, bw=394419 B/s, iops=24 , runt=300580msec
    clat (msec): min=8 , max=12826 , avg=1066.57, stdev=890.86
     lat (msec): min=8 , max=12826 , avg=1066.57, stdev=890.86
    clat percentiles (msec):
     |  1.00th=[   65],  5.00th=[  139], 10.00th=[  277], 20.00th=[  594],
     | 30.00th=[  734], 40.00th=[  848], 50.00th=[  947], 60.00th=[ 1057],
     | 70.00th=[ 1205], 80.00th=[ 1369], 90.00th=[ 1696], 95.00th=[ 2057],
     | 99.00th=[ 4555], 99.50th=[ 7373], 99.90th=[12387], 99.95th=[12518],
     | 99.99th=[12780]
    bw (KB/s)  : min=    1, max=   63, per=4.40%, avg=16.92, stdev= 7.77
  write: io=31683KB, bw=107325 B/s, iops=14 , runt=302286msec
    clat (usec): min=4 , max=22610K, avg=4745693.16, stdev=5250563.69
     lat (usec): min=4 , max=22610K, avg=4745693.73, stdev=5250563.65
    clat percentiles (usec):
     |  1.00th=[    5],  5.00th=[    8], 10.00th=[   14], 20.00th=[220160],
     | 30.00th=[741376], 40.00th=[1019904], 50.00th=[1433600], 60.00th=[7110656],
     | 70.00th=[8355840], 80.00th=[9109504], 90.00th=[11075584], 95.00th=[15007744],
     | 99.00th=[16711680], 99.50th=[16711680], 99.90th=[16711680], 99.95th=[16711680],
     | 99.99th=[16711680]
    bw (KB/s)  : min=    0, max=   60, per=6.16%, avg= 6.41, stdev= 8.89
    lat (usec) : 10=2.19%, 20=2.41%, 50=0.76%, 100=0.08%, 1000=0.01%
    lat (msec) : 2=0.02%, 10=0.02%, 20=0.06%, 50=0.50%, 100=1.97%
    lat (msec) : 250=5.63%, 500=4.96%, 750=12.25%, 1000=18.25%, 2000=30.15%
    lat (msec) : >=2000=20.74%
  cpu          : usr=0.00%, sys=0.00%, ctx=34248, majf=0, minf=4665
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=7236/w=4527/d=0, short=r=0/w=0/d=0

Run status group 0 (all jobs):
   READ: io=115776KB, aggrb=385KB/s, minb=385KB/s, maxb=385KB/s, mint=300580msec, maxt=300580msec
  WRITE: io=31682KB, aggrb=104KB/s, minb=104KB/s, maxb=104KB/s, mint=302286msec, maxt=302286msec

Disk stats (read/write):
    dm-0: ios=8177/10271, merge=0/0, ticks=1328277/1389664, in_queue=2717748, util=100.00%, aggrios=7504/9454, aggrmerge=669/1466, aggrticks=1227747/1157398, aggrin_queue=2384866, aggrutil=100.00%
  vda: ios=7504/9454, merge=669/1466, ticks=1227747/1157398, in_queue=2384866, util=100.00%
