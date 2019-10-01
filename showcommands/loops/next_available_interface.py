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

output = net_connect.send_command('show interfaces description', use_textfsm=True)
l = len(output)
for i in range(0,l):
    if output[i]['status'] != 'up':
        break
int = output[i]['port']
print ('\nFirst availble interface is ' + int)

string = ""
output2 = net_connect.send_command('show interfaces description', use_textfsm=True)
l = len(output2)
for i in range(0,l):
    if output2[i]['port'] == int and output2[i]['descrip'] != string:
        print ("Interface's description: " + output[i]['descrip'])

output3 = net_connect.send_command('show run interface ' + int, use_textfsm=True)
print ('\n---------------------------------------\n\n' + output3 + '\n---------------------------------------\n')

output4= net_connect.send_command('show interface switchport', use_textfsm=True)
l = len(output4)
for i in range(0,l):
    if output4[i]['interface'] == int:
        print (output4[i]['access_vlan'])

