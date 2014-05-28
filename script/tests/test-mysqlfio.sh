#!/bin/sh

echo 3 > /proc/sys/vm/drop_caches

#echo xxx > $1/xxx.res

fio small-mysql.fio | tee $1/test-mysqlfio.res

