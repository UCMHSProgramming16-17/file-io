# csvwriting.py
# import csv
import csv
import math

# open file in write mode
csvfile = open('triangles.csv', 'w', newline='')

# create the csv writer
csvwriter = csv.writer(csvfile, delimiter=',')

# write to t    he file
# create a header
csvwriter.writerow(['a', 'b', 'hypotenuse'])    

# for each value of a:
for a in range(1, 1001):

    # get each value of b:
    for b in range(a, 1001):
        hypotenuse = math.sqrt(a ** 2 + b ** 2)
        csvwriter.writerow([a, b, hypotenuse])

# close file
for a in range(1, 101):
    csvfile.close()
