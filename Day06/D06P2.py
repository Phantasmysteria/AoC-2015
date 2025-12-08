import sys
sys.path.append('..')
import aocutils
import numpy as np
import re

data = {}
data["00-raw"] = aocutils.listLines(day="06", part="2")
dataLength = len(data["00-raw"])

data["01-parsed"] = [[re.match("(.*[efn])", item).group(0), np.array([list(map(lambda x: int(x), i.split(","))) for i in re.findall("\\d*,\\d*", item)]).flatten()] for item in data["00-raw"]]

data["02-grid"] = np.zeros((1000, 1000), dtype=int)
gridY, gridX = np.shape(data["02-grid"])

for instruction in data["01-parsed"]:
    action = instruction[0]
    x1, y1, x2, y2 = instruction[1]

    data["02-grid"][y1:y2+1,x1:x2+1] = (lambda x: x+1 if action == 'turn on' else x-1 if action == 'turn off' else x+2)(data["02-grid"][y1:y2+1,x1:x2+1])
    data["02-grid"] = np.maximum(np.zeros((gridY, gridX), dtype=int), data["02-grid"], dtype=int)

output = np.sum(data["02-grid"])
print(output)

aocutils.outputToTextFile(data)