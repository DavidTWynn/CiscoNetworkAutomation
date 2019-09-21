from netmiko import ConnectHandler
from operator import itemgetter

RTR_10 = {
    'ip':   '192.168.0.10',
    'username': 'root',
    'password': 'cisco',
    'device_type': 'cisco_ios',
}

net_connect = ConnectHandler(**RTR_10)

output = net_connect.send_command('show ip int brie', use_textfsm=True)

l = len(output)
print ('\nList of interfaces which are UP \n')
for i in range(0,l):
    if output[i]['status'] == 'up':
        print (output[i]['intf'] +' ' + output[i]['status'])

print ('\nList of interfaces which are DOWN \n')
for i in range(0,l):
    if output[i]['status'] != 'up':
        print (output[i]['intf'] +' ' + output[i]['status'])
