import os
import csv


list_info = []
waste = {
    "temp": 0.0,
    "DO": 0.0,
    "pH": 0.0,   
    "conductivity": 0,
    "BOD": 0.0,
    "nitrate_n_nitrite": 0.0,
    "fecal_coliform": 0
}

def waste_input():
    waste["temp"] = float(input("Enter temperature: "))
    waste["DO"] = float(input("Enter dissolved oxygen (mg/l): "))
    waste["pH"] = float(input("Enter pH: "))
    waste["conductivity"] = int(input("Enter conductivity (mhos/cm): "))
    waste["BOD"] = float(input("Enter biochemical oxygen demand (mg/l): "))
    waste["nitrate_n_nitrite"] = float(input("Enter nitrate-n and nitrite-n (mg/l): "))
    waste["fecal_coliform"] = float(input("Enter fecal coliform (mpn/100ml): "))



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
