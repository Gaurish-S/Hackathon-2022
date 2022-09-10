import os
import csv


list_info = []


def parse_lake_data():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'waterquality.csv')
    
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            list_info.append ({
                "temp": row[3], 
                "DO" : row[4],
                "pH" : row[5],
                "conductivity" : row[6],
                "BOD" : row[7],
                "nitrate_n_nitrite": row[8],
                "fecal_coliform" : row[9], 
                "location" : row[1],
                "state" : row[2]
            })
        
        del list_info[0]
        print(list_info)

if __name__ == "__main__":
    parse_lake_data()
