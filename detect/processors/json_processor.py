import json
import sys

sys.path.append('..')
from constant.constant import KEYS_JSON

rootDir = '../'
ourDir = '../json/'

filename = rootDir + 'slot.txt'
endPoint = ourDir + 'slot.json'

prefix = 'w'

listSlots = {}
def handleJson():
    values = KEYS_JSON.values()
    upper_lat, upper_log, lower_lat, lower_log = values
    keys = [upper_lat, upper_log, lower_lat, lower_log]

    index = 1
    with open(filename) as slot:
        image = 0
        for line in slot:
            if (image != 0):
                coordinates = list(line.strip().split(None, 4))

                key = str(index)
                i = 0
                properties = {}
                while (i < len(coordinates)):
                    properties[keys[i]] = coordinates[i]
                    i = i + 1
                
                listSlots[key] = properties
                index = index + 1
            else:
                image = image + 1
                continue

    results = open(endPoint, prefix)
    json.dump(listSlots, results, indent = 4, sort_keys = True)

    results.close()

handleJson()
