#!/bin/sh

echo "====================================================================="
# Hostname
echo "HOSTNAME::"
hostname -s

echo ""
echo "---------------------------------------------------------------------"

# Product
dmidecode |grep -A8 "System Information" |grep "Product Name"|sed 's/^[ \t]*Product\ Name:/PRODUCT\t\t:/'
echo ""
echo "---------------------------------------------------------------------"

# CPU
echo "CPU::"
echo -e "cores\t\t:" `cat /proc/cpuinfo | grep "model name" |wc -l`
cat /proc/cpuinfo | grep -A 4 "model name" | grep -v stepping |head -3
echo ""
echo "---------------------------------------------------------------------"

# BIOS
echo "BIOS::"
dmidecode| grep -A3 "BIOS Information"| grep Version |sed 's/^[ \t]*Version:\ /Version\t\t:/'
echo ""
echo "---------------------------------------------------------------------"

# Memory
echo "MEMORY::"
echo "Total: " `free  | grep Mem | awk '{print $2}'`
echo ""
echo "---------------------------------------------------------------------"

# Harddisk
echo "LOCAL DISK::"
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT

echo ""
echo "---------------------------------------------------------------------"

# Partitions
echo "PARTITIONS::"
df -ha

echo ""
echo "---------------------------------------------------------------------"

# Networks
echo "NETWORKS::"

for INTF in `ifconfig -a | grep HWaddr | awk '{print $1}'`
do
    ifconfig $INTF | grep "inet addr" -B1
    x=`ifconfig $INTF | grep "inet addr" -B1`
    if [ -n "$x" ]; then
        ethtool $INTF | grep "Link detected"
    fi
done
echo ""

echo "BRIDGES::"

brctl show

echo ""

echo "ROUTE::"

route -n

echo ""

echo "====================================================================="