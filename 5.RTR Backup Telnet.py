import getpass
import telnetlib

user = input("Telnet Username: ")
password = getpass.getpass()

IP_File = open('Devices.txt')

for ip in IP_File:
    ip = ip.strip()
    print('Getting running config from RTR ' + ip)
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b"enable\n")
    tn.write((input('Please input secret: ')).encode('ascii') + b"\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b'exit\n')

    Read_Lines = tn.read_all()
    Save_Lines = open("RTR - " + HOST + '.txt', "w")
    Save_Lines.write(Read_Lines.decode('ascii'))
    Save_Lines.write("\n")
    Save_Lines.close()
    print(tn.read_all().decode('ascii'))
