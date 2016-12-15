# csvwriting.py
# import csv 
import csv
import math

# open csvfile
csvfile = open('triangles.csv', 'w', newline='')

# create csvwriter
csvwriter = csv.writer(csvfile, delimiter=',')

# write to file
# a, b, hypotenuse
csvwriter.writerow(['a', 'b', 'hypotenuse'])
# write numbers 1-100 into the first cell of the next 100 rows
for a in range(1, 101):
    # get each possible value of b
    for b in range(a, 101):
        # calculate hypotenuse
        hypotenuse = math.sqrt(a **2 + b ** 2)
        # write a row containing a, b, hypotenuse
        csvwriter.writerow([a, b, hypotenuse])
# close file
csvfile.close()