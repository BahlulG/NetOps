# Find similar lines

with open('file_1.txt', 'r') as file1, open('file_2.txt', 'r') as file2:
    same = set(file1).intersection(file2)

same.discard('\n')

with open('output_same.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

# ===================================================== #

# Find different lines


with open('file_1.txt', 'r') as file1, open('file_2.txt', 'r') as file2:
    difference1 = set(file1).difference(file2)

with open('file_1.txt', 'r') as file1, open('file_2.txt', 'r') as file2:
    difference2 = set(file2).difference(file1)

difference1.discard('\n')
difference2.discard('\n')

with open('output_diff.txt', 'w') as file_out:
    for line in difference1:
        file_out.write(line)

with open('output_diff.txt', 'a') as file_out:
    for line in difference2:
        file_out.write(line)
