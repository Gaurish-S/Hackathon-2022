import os
import csv

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

def parse_lake_data():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'waterquality.csv')
    
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        i = -1
        for row in reader:
            list_info[i] = {
                "temp": row[3], 
                "DO" : row[4],
                "pH" : row[5],
                "conductivity" : row[6],
                "BOD" : row[7],
                "nitrate_n_nitrite": row[8],
                "fecal_coliform" : row[9], 
                "location" : row[1],
                "state" : row[2]
            }
            i+=1
    print(list_info)
if __name__ == "__main__":
    parse_lake_data()