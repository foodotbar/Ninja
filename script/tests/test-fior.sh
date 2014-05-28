#!/bin/sh

echo 3 > /proc/sys/vm/drop_caches

FILENAME=fiofile1
RUNTIME=60
SIZE=1g
BLOCKSIZE=4k
IOENGINE=sync
RESULTFILE=test-fior.res
RATEIOPS=100

fio --readonly --readwrite=read --bs=$BLOCKSIZE --size=$SIZE --runtime=$RUNTIME --rate_iops=$RATEIOPS --iodepth=1 --filename=$FILENAME --ioengine=$IOENGINE --direct=1 --name=iops_randread --group_reporting | tee $1/$RESULTFILE

#fio --readonly --readwrite=randread --bs=$BLOCKSIZE --size=$SIZE --runtime=$RUNTIME --rate_iops=$RATEIOPS --iodepth=1 --filename=$FILENAME --ioengine=$IOENGINE --direct=1 --name=iops_randread --group_reporting  | tee $1/$RESULTFILE

#fio --readwrite=write --bs=$BLOCKSIZE --size=$SIZE --runtime=$RUNTIME --iodepth=1 --rate_iops=$RATEIOPS --filename=$FILENAME --ioengine=$IOENGINE --direct=1 --name=iops_write --group_reporting  | tee $1/$RESULTFILE

#fio --readwrite=randwrite --bs=$BLOCKSIZE --size=$SIZE --runtime=$RUNTIME --iodepth=1 --rate_iops=$RATEIOPS --filename=$FILENAME --ioengine=$IOENGINE --direct=1 --name=iops_read --group_reporting  | tee $1/$RESULTFILE

#fio --readwrite=randrw --rwmixread=67 --bs=$BLOCKSIZE --size=$SIZE --runtime=$RUNTIME --iodepth=1 --rate_iops=$RATEIOPS --filename=$FILENAME --ioengine=$IOENGINE --direct=1 --name=iops_randrw --group_reporting  | tee $1/$RESULTFILE
