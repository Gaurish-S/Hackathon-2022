# Assuming that csv file is present in another file named DatasetOfLakes.csv

import csv

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

    return waste






