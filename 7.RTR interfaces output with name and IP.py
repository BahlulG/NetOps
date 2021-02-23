# Router Interfaces output with name and address
from netmiko import ConnectHandler

with open('RTRs.txt') as ip_list:
    devices = ip_list.readlines()

device_type = 'cisco_ios'
port = 22
verbose = True

for device in range(len(devices)):
    print('Connecting to Device: ' + devices[device].strip(), '\n')
    net_connect = ConnectHandler(ip=devices[device].strip(), device_type=device_type,
                                 username=input('Enter Username: '),
                                 password=input('Enter Password: '), secret=input('Enter Secret: '))

    prompter = net_connect.find_prompt()  # "find_prompt()" - Return the current router prompt
    if '>' in prompter:
        net_connect.enable()  # "enable()" - Enter enable mode

    output = net_connect.send_command('show ip interface brief')

    with open('int.txt', 'w') as file:
        file.write(output)

    with open('int.txt') as file:
        a = file.readlines()
        int_column = 0
        for x in a[1:]:
            print('Interface: ' + x.split()[int_column])
            print('IP-Address: ' + x.split()[int_column + 1], '\n')
