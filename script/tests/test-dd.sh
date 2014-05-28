#!/bin/sh

echo 3 > /proc/sys/vm/drop_caches
sleep 5

rm -f /tmp/result.txt
echo "Whole test's start time: "$(date) >> ${1}/test-dd.res
echo "no direct write start time: "$(date) >> ${1}/test-dd.res
dd if=/dev/zero of=/tmp/xx  bs=10M count=100 > /tmp/result.txt 2>&1
stoptime=$(date)
RST=`cat /tmp/result.txt| grep bytes | awk '{print $8}'`

echo "no direct write: "$RST" MB/s" >> ${1}/test-dd.res
echo "no direct write end time: "$stoptime >> ${1}/test-dd.res
echo 3 > /proc/sys/vm/drop_caches
sleep 5

rm -f /tmp/result.txt

echo "direct write start time: "$(date) >> ${1}/test-dd.res

dd if=/dev/zero of=/tmp/xx oflag=direct bs=10M count=100 > /tmp/result.txt 2>&1
stoptime=$(date)
RST=`cat /tmp/result.txt| grep bytes | awk '{print $8}'`

echo "direct write: "$RST" MB/s" >> ${1}/test-dd.res

echo "direct write end time: "$stoptime >> ${1}/test-dd.res

echo 3 > /proc/sys/vm/drop_caches
sleep 5

rm -f /tmp/result.txt

echo "no direct read start time: "$(date) >> ${1}/test-dd.res

dd if=/tmp/xx of=/dev/null  bs=10M count=100 > /tmp/result.txt 2>&1
stoptime=$(date)
RST=`cat /tmp/result.txt| grep bytes | awk '{print $8}'`

echo "no direct read: "$RST" MB/s" >> ${1}/test-dd.res

echo "no direct read end time: "$stoptime >> ${1}/test-dd.res

echo 3 > /proc/sys/vm/drop_caches
sleep 5

rm -f /tmp/result.txt

echo "direct read start time: "$(date) >> ${1}/test-dd.res

dd if=/tmp/xx of=/dev/null iflag=direct bs=10M count=100 > /tmp/result.txt 2>&1
stoptime=$(date)
RST=`cat /tmp/result.txt| grep bytes | awk '{print $8}'`

echo "direct read: "$RST" MB/s" >> ${1}/test-dd.res

echo "direct read end time: "$stoptime >> ${1}/test-dd.res
