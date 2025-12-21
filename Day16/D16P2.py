import sys
sys.path.append('..')
import aocutils
import re
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="16", part="2")
dataLength = len(data["00-raw"])

parsePattern = "([a-zA-Z]+): (\\d+), ([a-zA-Z]+): (\\d+), ([a-zA-Z]+): (\\d+)"

data["01-parsed"] = [re.search(parsePattern, item) for item in data["00-raw"]]

belongings = ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes']
belongingsMap = {v: k for k, v in enumerate(belongings)}
quantities = np.array([3, 7, 2, 3, 0, 0, 5, 3, 2, 1])

data["02-suesBelongings"] = []
for item in data['01-parsed']:
    belonging = np.full_like(quantities, -1, dtype=int)
    for i in range(1, 7, 2):
        belonging[belongingsMap[item.group(i)]] = int(item.group(i+1))
    data['02-suesBelongings'].append(belonging)

data["02-suesBelongings"] = np.array(data["02-suesBelongings"])

def elementCheck(arr, target, index, operation):
    if arr[index] == -1:
        return True
    match operation:
        case '==':
            return arr[index] == target[index]
        case '>':
            return arr[index] > target[index]
        case '<':
            return arr[index] < target[index]

def sueCheck(arr):
    return elementCheck(arr, quantities, 0, '==') \
        and elementCheck(arr, quantities, 1, '>') \
        and elementCheck(arr, quantities, 2, '==') \
        and elementCheck(arr, quantities, 3, '<') \
        and elementCheck(arr, quantities, 4, '==') \
        and elementCheck(arr, quantities, 5, '==') \
        and elementCheck(arr, quantities, 6, '<') \
        and elementCheck(arr, quantities, 7, '>') \
        and elementCheck(arr, quantities, 8, '==') \
        and elementCheck(arr, quantities, 9, '==') 

data["03-sueCompare"] = np.apply_along_axis(sueCheck, arr=data['02-suesBelongings'], axis=1)

data["04-correctSue"] = np.where(data['03-sueCompare'] == True)[0] + 1

output = data["04-correctSue"][0]
print(output)

aocutils.outputToTextFile(data)