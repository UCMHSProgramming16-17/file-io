# open file in write mode
file = open('listfile.txt', 'w')

# TODO: create the list
for n in range(10):
    file.write(input('SPEAK! ') + '\n')


# close file
file.close()