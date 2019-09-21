from netmiko import ConnectHandler
from operator import itemgetter
from getpass import getpass
import readline

RTR_10 = {
    'ip': input("Enter device IP: "),
    'username': 'root',
    'password': getpass(),
    'device_type': 'cisco_ios',
}
print ('Checking interface status..')
net_connect = ConnectHandler(**RTR_10)

output = net_connect.send_command('show ip int brie', use_textfsm=True)

name = output[1]['intf']
status = output[1]['status']
print ('\nInterface ' + name + ' status is ' + status )

if status == 'up':
    print ('Finishing the script')
else :
    print ('making backup interface UP')
    config_commands = [ 'int fa0/1',
                        'no shut' ]
    output = net_connect.send_config_set(config_commands)
    print (output)
    print ('Finished configuration')
