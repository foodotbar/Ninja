#!/usr/bin/expect -f  

set VMIP [lindex $argv 0]
set VMuser root
set VMPW 123456
set hostPW westlake
#spawn ssh-keygen -t rsa -N \"\" -f ~/.ssh/id_rsa
#expect "*y/n" 
#send "y\r"
#spawn ssh-add 
#spawn ssh-copy-id -i $VMuser@$VMIP
#echo -e "\n\n\n" | ssh-keygen -t rsa
#spawn ./keygen.sh
#spawn ./copyid.sh
#spawn sleep 3
spawn ssh-copy-id  $VMuser@$VMIP
expect {
 "*yes/no" { send "yes\r"; exp_continue}
 "*password:"  {send "$VMPW\r" }
}

spawn ssh $VMuser@$VMIP       
expect {                   
 "*yes/no" { send "yes\r"; exp_continue}  
 "*password:" { send "$VMPW\r" }      
}
expect "#*"  
send "rm -f /root/.ssh/known_hosts \r"
send "ssh-keygen -t rsa -N \"\" -f ~/.ssh/id_rsa \r"
expect "*y/n"
send "y\r"
send "ssh-copy-id -i ~/.ssh/id_rsa.pub root@testhost \r"
expect {
 "*yes/no" { send "yes\r"; exp_continue}
 "*password:"  {send "$hostPW\r" }
}

expect "#*"
send "exit \r"
expect eof
