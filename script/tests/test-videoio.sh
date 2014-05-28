#!/bin/sh

echo 3 > /proc/sys/vm/drop_caches
sleep 5

iozone -i0 -i2 -i5 -i8 -r 64k -s 400m -f /tmp/iozone.tmp -ecp -K > ${1}/test-videoio.res


