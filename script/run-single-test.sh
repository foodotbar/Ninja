#!/bin/sh

cd script
RESULTDIR=`pwd`/results
cd tests

mkdir $RESULTDIR >/dev/null 2>&1
rm -rf $RESULTDIR/*

TEST=$1
sleep 5
echo Now running $TEST ...
./nmon -F $RESULTDIR/$TEST.nmon -s5
./${TEST}.sh $RESULTDIR
pkill nmon

cd ..
RESULTFILE=`hostname -s`.`date +%Y-%m-%d_%H-%M-%S`.$TEST.tar.gz

tar czf $RESULTFILE -C results/ .
scp $RESULTFILE root@testhost:/root/Desktop/workdir/result/`hostname -s`/
