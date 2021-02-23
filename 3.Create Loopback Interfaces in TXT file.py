import sys

n = int(input('Please make your input as integer: '))


def lo_int(i):
    c = 1
    b = 1
    c1 = 254
    c3 = 1
    for i in range(n):
        if c <= 253:
            with open('lo_int.txt', 'a') as file:
                sys.stdout = file
                print('interface loop ', c, '\nip address', '{0}.1.1.{1}'.format(b, c), '\nno shut', '\nexit', '\n')
                c += 1
        else:
            if c3 <= 253:
                b = 2
                with open('lo_int.txt', 'a') as file:
                    sys.stdout = file
                    print('interface loop ', c1, '\nip address', '{0}.1.1.{1}'.format(b, c3), '\nno shut', '\nexit', '\n')
                    c1 += 1
                    c3 += 1
            else:
                with open('lo_int.txt', 'a') as file:
                    sys.stdout = file
                    print('Cannot create Loop-Back interface with IP Address 254, Breaking')
                    break


lo_int(n)
