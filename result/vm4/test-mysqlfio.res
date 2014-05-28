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

mysql-binlog: (groupid=0, jobs=160): err= 0: pid=2930: Tue Jan  7 16:55:33 2014
  read : io=145824KB, bw=497275 B/s, iops=30 , runt=300284msec
    clat (msec): min=2 , max=10675 , avg=842.79, stdev=755.91
     lat (msec): min=2 , max=10675 , avg=842.79, stdev=755.91
    clat percentiles (msec):
     |  1.00th=[   48],  5.00th=[  105], 10.00th=[  229], 20.00th=[  433],
     | 30.00th=[  529], 40.00th=[  619], 50.00th=[  725], 60.00th=[  848],
     | 70.00th=[  988], 80.00th=[ 1139], 90.00th=[ 1385], 95.00th=[ 1598],
     | 99.00th=[ 4113], 99.50th=[ 5997], 99.90th=[10159], 99.95th=[10290],
     | 99.99th=[10683]
    bw (KB/s)  : min=    1, max=   93, per=4.31%, avg=20.90, stdev= 9.97
  write: io=39955KB, bw=135719 B/s, iops=18 , runt=301456msec
    clat (usec): min=3 , max=28301K, avg=3815334.86, stdev=4531880.45
     lat (usec): min=4 , max=28301K, avg=3815335.51, stdev=4531880.43
    clat percentiles (usec):
     |  1.00th=[    5],  5.00th=[    9], 10.00th=[   14], 20.00th=[199680],
     | 30.00th=[544768], 40.00th=[806912], 50.00th=[1171456], 60.00th=[4685824],
     | 70.00th=[5341184], 80.00th=[8093696], 90.00th=[9109504], 95.00th=[10158080],
     | 99.00th=[16711680], 99.50th=[16711680], 99.90th=[16711680], 99.95th=[16711680],
     | 99.99th=[16711680]
    bw (KB/s)  : min=    0, max=   74, per=5.70%, avg= 7.52, stdev=10.48
    lat (usec) : 4=0.01%, 10=1.91%, 20=2.66%, 50=0.84%, 100=0.03%
    lat (usec) : 250=0.01%, 1000=0.01%
    lat (msec) : 2=0.01%, 4=0.01%, 10=0.01%, 20=0.06%, 50=0.91%
    lat (msec) : 100=2.78%, 250=5.24%, 500=12.61%, 750=19.78%, 1000=14.39%
    lat (msec) : 2000=20.71%, >=2000=18.01%
  cpu          : usr=0.00%, sys=0.00%, ctx=43255, majf=0, minf=4661
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=9114/w=5685/d=0, short=r=0/w=0/d=0

Run status group 0 (all jobs):
   READ: io=145824KB, aggrb=485KB/s, minb=485KB/s, maxb=485KB/s, mint=300284msec, maxt=300284msec
  WRITE: io=39954KB, aggrb=132KB/s, minb=132KB/s, maxb=132KB/s, mint=301456msec, maxt=301456msec

Disk stats (read/write):
    dm-0: ios=9175/12801, merge=0/0, ticks=1222208/1371336, in_queue=2593566, util=100.00%, aggrios=9175/11835, aggrmerge=0/1795, aggrticks=1222189/1146540, aggrin_queue=2368707, aggrutil=100.00%
  vda: ios=9175/11835, merge=0/1795, ticks=1222189/1146540, in_queue=2368707, util=100.00%
