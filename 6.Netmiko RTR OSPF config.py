# SSH OSPF Config
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
    print('\n')
    prompter = net_connect.find_prompt()  # "find_prompt()" - Return the current router prompt
    if '>' in prompter:
        net_connect.enable()  # "enable()" - Enter enable mode

    output = net_connect.send_command('show run | sec ospf')

    with open('{0}.txt'.format(devices[device].strip())) as config_lines:
        config = config_lines.readlines()

    if 'router ospf' not in output:
        print('OSPF is not enabled on device: ' + devices[device].strip())
        advice_OSPF = input(
            'Would you like you to enable default OSPF settings on: ' + devices[device].strip() + ' <y/n> ')
        if advice_OSPF == 'y':
            output = net_connect.send_config_set(config)
            print(output)
            print('OSPF is now configured!', '\n')
        else:
            print('No OSPF configurations have been made!', '\n')

    else:
        print('OSPF is already configured on {}.'.format(devices[device].strip()),
              '\nNo additional changes needed', '\n')
