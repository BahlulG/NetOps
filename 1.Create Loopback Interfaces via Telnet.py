import getpass
import telnetlib

HOST = "10.51.121.246"
user = input("Telnet Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write((input('Please input secret: ')).encode('ascii') + b"\n")
tn.write(b"conf t\n")

for i in range(1, int(input('Input highest Loopback interface number: '))):
    tn.write(b"int loop " + str(i).encode('ascii') + b"\n")
    tn.write(b"ip address 10.10.10." + str(i).encode('ascii') + b" 255.255.255.255" + b"\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
