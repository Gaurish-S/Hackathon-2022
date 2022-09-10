import parsecsv

def getDifference():
    waste_info = parsecsv.waste()
    target_info = parsecsv.list_info()

    for target in target_info:
        for key in waste_info:
            if waste_info[key].isNumeric() & target_info.has_key(key):
                difference = key + "Diff"
                target_info[difference] = abs(waste_info[key] - target_info[key])

def getSalinity():
    joined_list = parsecsv.list_info.append(parsecsv.waste)

    for entry in joined_list:
        if entry.has_key("conductivity"):
            if entry["conductivity"] > 0.1 & entry["conductivity"] < 5:
                entry["salinity"] = 640 * entry["conductivity"]
            elif entry["conductivity"] > 5:
                entry["salinity"] = 800 * entry["conductivity"]
            else:
                return -1
