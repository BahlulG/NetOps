# Entire file difference
with open('file_1.txt', 'r') as file1, open('file_2.txt', 'r') as file2:
    a = file1.readlines()
    b = file2.readlines()


if len(a) > len(b):
    for i in set(a):
        if i not in set(b):
            with open('not_in.txt', 'a') as file1:
                file1.write(i)
else:
    for i in set(b):
        if i not in set(a):
            with open('not_in.txt', 'a') as file1:
                file1.write(i)
