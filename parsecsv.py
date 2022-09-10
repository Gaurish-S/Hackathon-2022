# Assuming that csv file is present in another file named DatasetOfLakes.csv

import csv

csv_filename = 'DatasetOfLakes.csv'
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
