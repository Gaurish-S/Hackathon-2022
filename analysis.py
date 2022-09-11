import parsecsv
import statistics

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def getDifference():
    waste_info = parsecsv.waste
    target_info = parsecsv.list_info.copy()

    for target in target_info:
        for key in target:
            if is_float(target[key]) & (key in waste_info):
                difference = key + "Diff"
                target[difference] = float(waste_info[key]) - float(target[key])

def appendSalinity():
    joined_list = parsecsv.list_info.append(parsecsv.waste)

    for entry in joined_list:
        if entry.has_key("conductivity"):
            # differing constants are required for salinity calculations
            if entry["conductivity"] > 0.1 & entry["conductivity"] < 5:
                entry["salinity"] = 640 * entry["conductivity"]
            elif entry["conductivity"] > 5:
                entry["salinity"] = 800 * entry["conductivity"]
            else:
                return -1

def targetsMean():
    target_info = parsecsv.list_info
    
    # intermediate dictionary of list of numeric factor values
    calcDict = {}
    for entry in target_info:
        for key in entry:
            if not entry[key].isnumeric():
                continue
            else:
                calcDict[key + "Mean"].append(entry[key])

    # will be a dictionary of mean values
    meanDict = {}
    for factorKey in calcDict:
        meanDict[factorKey] = (statistics.fmean(calcDict[factorKey]))

    return meanDict

# Z = (X - µ)/σ or (x - mean) / stdev
# standard deviations away from the mean = mean +/- 
def GetzScores():
    waste_info = parsecsv.waste
    target_info = parsecsv.list_info

    meanDict = targetsMean()

    zScoresDict = {}
    for factor in waste_info:
        for target in target_info:
            if waste_info[factor].isNumeric() & waste_info.has_key(factor):
                zScoresDict[factor + " stdev"] = (waste_info[factor] - meanDict[factor + "Mean"])/statistics.stdev(target_info)

    return zScoresDict
    

parsecsv.parse_lake_data()
getDifference()
print(parsecsv.list_info)

