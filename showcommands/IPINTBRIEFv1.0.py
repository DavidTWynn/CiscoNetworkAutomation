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
print(output)

print(output[3])

l = len(output)
print ('\nTotal number of interfaces are ' + str(l))

name = output[1]['intf']
status = output[1]['status']
print ('\nInterface ' + name + ' status is ' + status )

interface0 = output[1]
getint = itemgetter('intf')
getstatus =  itemgetter('status')
name = getint(interface0)
status = getstatus(interface0)
print ('\nInterface ' + name + ' status is ' + status )
