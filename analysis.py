import parsecsv
import statistics
import copy

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

def getDifference():
    waste_info = parsecsv.waste
    new_list_info = []
    for target in parsecsv.list_info:
        new_target = copy.deepcopy(target)
        for key in target:
            if is_float(target[key]) & (key in waste_info):
                difference = key + "Diff"
                new_target[difference] = abs(float(waste_info[key]) - float(target[key]))
            elif (target[key] == "NA") & (key in waste_info):
                difference = key + "Diff"
                new_target[difference] = float("inf")
        new_list_info.append(new_target)
    
    return new_list_info


def appendSalinity():
    waste_info = parsecsv.waste
    new_list_info = []
    for target in parsecsv.list_info:
        new_target = copy.deepcopy(target)
        if ("conductivity" in target) & (target["conductivity"] != "NA"):
            new_target["salinity"] = calcSalinity(float(target["conductivity"]))
        
        new_list_info.append(new_target)

    if ("conductivity" in parsecsv.waste):
        parsecsv.waste["salinity"] = calcSalinity(float(waste_info["conductivity"]))

    return new_list_info

# note that the specific conversion may depend on the type of water itself with most
# sources citing 
# TDS (mg/L or ppm) = EC (dS/m) x 640 (EC from 0.1 to 5 dS/m)
# TDS (mg/L or ppm) = EC (dS/m) x 800 (EC > 5 dS/m)

def calcSalinity(conductivity):
    # differing constants are required for salinity calculations
    if (conductivity > 0.1) & (conductivity < 5):
        return 640 * conductivity
    elif (conductivity > 5):
        return 800 * conductivity
    else:
        return 0

def targetsMean():
    waste_info = parsecsv.waste
    target_info = parsecsv.list_info

    calcDict = {}
    for target in parsecsv.list_info:
        new_target = copy.deepcopy(target)
        for key in target:
            if is_float(target[key]) & (key in waste_info):
                new_key = key + "Mean"
                if (new_key in calcDict):
                    calcDict[key + "Mean"].append(float(target[key]))
                else:
                    calcDict[key + "Mean"] = [(float(target[key]))]
    meanDict = {}
    for factorKey in calcDict:
        meanDict[factorKey] = (sum(calcDict[factorKey])/len(calcDict[factorKey]))
    
    return meanDict

def targetsStdev():
    waste_info = parsecsv.waste
    target_info = parsecsv.list_info

    calcDict = {}
    for target in parsecsv.list_info:
        new_target = copy.deepcopy(target)
        for key in target:
            if is_float(target[key]) & (key in waste_info):
                new_key = key + "Stdev"
                if (new_key in calcDict):
                    calcDict[key + "Stdev"].append(float(target[key]))
                else:
                    calcDict[key + "Stdev"] = [(float(target[key]))]
    stdevDict = {}
    for factorKey in calcDict:
        stdevDict[factorKey] = (statistics.stdev(calcDict))
    
    return stdevDict
# Z = (X - µ)/σ or (x - mean) / stdev
# standard deviations away from the mean = mean +/- 
def GetzScores():
    waste_info = parsecsv.waste
    target_info = parsecsv.list_info

    meanDict = targetsMean()
    stdevDict = targetsStdev()

    zScoresDict = {}
    for factor in waste_info:
        if is_float(waste_info[factor]) & ((factor + "Mean") in meanDict):
            zScoresDict[factor + " stdev"] = (float(waste_info[factor]) - float(meanDict[factor + "Mean"]))/float(stdevDict[factor + "Stdev"])

    return zScoresDict
    


