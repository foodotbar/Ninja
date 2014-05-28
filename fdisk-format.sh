#!/bin/bash

#sometimes need dmsetup remove /dev/mapper/xx

for i in "e" "f" "g"; do

umount /disk-"$i" > /dev/null 2>&1
#	fdisk /dev/sd"$i" << EOF
#n
#p
#1
#
#
#w
#EOF

dd if=/dev/zero of=/dev/sd"$i" bs=1k count=1000

mkfs.ext4 -m0 -O extent,has_journal -T largefile4 -F /dev/sd"$i"
#e2label /dev/sd"$i" sd"$i"
mkdir /disk-"$i" >/dev/null 2>&1
mount -o,noatime -t ext4 /dev/sd"$i" /disk-"$i"
done
