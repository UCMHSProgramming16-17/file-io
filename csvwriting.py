# csvwriting.py
# import module
import csv
import math

# create file
# newline='' is only needed on Windows
csvfile = open('csvexample.csv', 'w', newline='')

# create csvwriter
csvwriter = csv.writer(csvfile, delimiter=',')

# write information
csvwriter.writerow(['a', 'b', 'hypotenuse'])
for a in range(1, 101):
    for b in range(a, 101):
        hypotenuse = math.sqrt(a ** 2 + b ** 2)
        csvwriter.writerow([a, b, hypotenuse])

# close file
csvfile.close()