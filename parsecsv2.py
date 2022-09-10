import os
import csv
dirname = os.path.dirname(__file__)
print(__file__)
print(dirname)

filename = os.path.join(dirname, 'waterquality.csv')
print(filename)
with open(filename, 'r') as csv_file:
     reader = csv.reader(csv_file)

     for row in reader:
         print(row)
