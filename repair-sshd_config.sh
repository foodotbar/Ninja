#!/bin/sh

sed -i "s/#UseDNS\ yes/UseDNS\ no/g" /etc/ssh/sshd_config

 ./exec-on-all.py 'sed -i "s/#UseDNS\ yes/UseDNS\ no/g" /etc/ssh/sshd_config'
