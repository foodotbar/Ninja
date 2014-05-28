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

mysql-binlog: (groupid=0, jobs=160): err= 0: pid=2880: Tue Jan  7 16:54:26 2014
  read : io=124160KB, bw=422959 B/s, iops=25 , runt=300596msec
    clat (msec): min=4 , max=5040 , avg=986.12, stdev=604.63
     lat (msec): min=4 , max=5040 , avg=986.12, stdev=604.63
    clat percentiles (msec):
     |  1.00th=[   53],  5.00th=[  121], 10.00th=[  269], 20.00th=[  553],
     | 30.00th=[  685], 40.00th=[  807], 50.00th=[  922], 60.00th=[ 1045],
     | 70.00th=[ 1188], 80.00th=[ 1352], 90.00th=[ 1598], 95.00th=[ 1958],
     | 99.00th=[ 3294], 99.50th=[ 4015], 99.90th=[ 4752], 99.95th=[ 4817],
     | 99.99th=[ 5014]
    bw (KB/s)  : min=    3, max=   84, per=4.25%, avg=17.56, stdev= 8.22
  write: io=34072KB, bw=115377 B/s, iops=16 , runt=302391msec
    clat (usec): min=4 , max=18006K, avg=4363751.68, stdev=4589514.09
     lat (usec): min=4 , max=18006K, avg=4363752.25, stdev=4589514.11
    clat percentiles (usec):
     |  1.00th=[    5],  5.00th=[    8], 10.00th=[   14], 20.00th=[216064],
     | 30.00th=[692224], 40.00th=[1003520], 50.00th=[1368064], 60.00th=[6717440],
     | 70.00th=[8355840], 80.00th=[9109504], 90.00th=[9764864], 95.00th=[12386304],
     | 99.00th=[15663104], 99.50th=[16449536], 99.90th=[16711680], 99.95th=[16711680],
     | 99.99th=[16711680]
    bw (KB/s)  : min=    0, max=   70, per=5.74%, avg= 6.43, stdev= 9.14
    lat (usec) : 10=2.50%, 20=2.13%, 50=0.84%, 100=0.08%
    lat (msec) : 2=0.01%, 4=0.02%, 10=0.03%, 20=0.14%, 50=0.62%
    lat (msec) : 100=2.14%, 250=5.64%, 500=5.96%, 750=13.91%, 1000=16.02%
    lat (msec) : 2000=29.96%, >=2000=20.00%
  cpu          : usr=0.00%, sys=0.00%, ctx=36888, majf=0, minf=4657
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued    : total=r=7760/w=4904/d=0, short=r=0/w=0/d=0

Run status group 0 (all jobs):
   READ: io=124160KB, aggrb=413KB/s, minb=413KB/s, maxb=413KB/s, mint=300596msec, maxt=300596msec
  WRITE: io=34071KB, aggrb=112KB/s, minb=112KB/s, maxb=112KB/s, mint=302391msec, maxt=302391msec

Disk stats (read/write):
    dm-0: ios=8443/11088, merge=0/0, ticks=1182067/1371850, in_queue=2553959, util=100.00%, aggrios=7950/10230, aggrmerge=479/1601, aggrticks=1115561/1131161, aggrin_queue=2246692, aggrutil=100.00%
  vda: ios=7950/10230, merge=479/1601, ticks=1115561/1131161, in_queue=2246692, util=100.00%
