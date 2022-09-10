import os
import csv

def parse_lake_data():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'waterquality.csv')
    list_info = {
        "temp":0.0,
        "DO" : 0.0,
        "pH" : 0.0,
        "conductivity" : 0,
        "BOD" : 0.0,
        "nitrate_n_nitrite": 0.0,
        "fecal_coliform" : 0, 
        "location" : "null",
        "state" : "null"
    }
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        i = 2
        for row in reader:
            list_info[i] = {
                "temp": row[4], 
                "DO" : row[5],
                "pH" : row[6],
                "conductivity" : row[7],
                "BOD" : row[8],
                "nitrate_n_nitrite": row[9],
                "fecal_coliform" : row[10], 
                "location" : row[2],
                "state" : row[3]
            }
            i+=1
    print (list_info)
if __name__ == "__main__":
    parse_lake_data()