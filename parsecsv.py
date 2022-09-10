import os
import csv

waste = {
    "temp": 0.0,
    "DO": 0.0,
    "pH": 0.0,   
    "conductivity": 0.0,
    "BOD": 0.0,
    "nitrate_n_nitrite": 0.0,
    "fecal_coliform": 0.0
}

def set_waste(attribute, input_str):
    global waste
    waste[attribute] = float(input_str)

def show_waste(attribute):
    print(waste[attribute])

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
