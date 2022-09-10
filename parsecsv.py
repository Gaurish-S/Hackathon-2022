import os
import csv

def parse_lake_data():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'waterquality.csv')

    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            print(row)

if __name__ == "__main__":
    parse_lake_data()