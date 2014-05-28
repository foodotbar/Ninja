#!/bin/sh

cd script
RESULTDIR=`pwd`/results
cd tests

mkdir $RESULTDIR >/dev/null 2>&1
rm -rf $RESULTDIR/*

for TEST in `ls *.sh`
do
	sleep 5
	echo Now running $TEST ...
	./nmon -F $RESULTDIR/$TEST.nmon -s5
	./$TEST $RESULTDIR
	pkill nmon
done

cd ..
RESULTFILE=`hostname -s`.`date +%Y-%m-%d_%H-%M-%S`.tar.gz
#cp /root/uptime /root/booted results/
tar czf $RESULTFILE -C results/ .
scp $RESULTFILE root@testhost:/root/Desktop/workdir/result/`hostname -s`/
