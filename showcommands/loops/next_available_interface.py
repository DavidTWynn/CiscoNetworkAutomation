from netmiko import ConnectHandler
from operator import itemgetter
from getpass import getpass
import readline

NETDEVICE1 = {
#    'ip': input("Enter device IP: "),
    'username': 'root',
#    'password': getpass(),
     'ip': '192.168.0.10',
     'password': 'cisco',
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**NETDEVICE1)

output = net_connect.send_command('show ip interface brief', use_textfsm=True)

l = len(output)
for i in range(0,l):
    if output[i]['status'] != 'up':
        break
int = output[i]['intf']
print ('\nFirst availble interface is ' + output[i]['intf'])

output2 = net_connect.send_command('show mac address-table', use_textfsm=True)

print (output2)
print (int)

l = len(output2)
for i in range(0,l):
    if output2[i]['destination_port'] == int:
        print (output2)
    else:
        print ('There are no mac addresses found on that interface')
        break

output3 = net_connect.send_command('show interfaces description', use_textfsm=True)

l = len(output3)
for i in range(0,l):
    if output3[i]['port'] == int:
        print (output[i])

