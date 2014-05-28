#!/bin/sh
rm -f /root/.ssh/*
/usr/bin/ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa
