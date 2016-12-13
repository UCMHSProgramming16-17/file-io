# open file
file = open('list.txt', 'w')

# TODO: write list to file
for n in range(10):
    file.write(str(n) + input('SPEAK! ') + '\n')

# close file
file.close()