import sys
sys.path.append('..')
import aocutils
import math
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="02", part="2")
dataLength = len(data["00-raw"])

data["01-sides"] = np.array([[int(x) for x in item.split("x")] for item in data["00-raw"]])
# now this is some quality math equation
data["02-ribbon"] = np.apply_along_axis(lambda arr: 2 * (np.sum(arr) - np.amax(arr)) + np.prod(arr), axis=1, arr=data["01-sides"])

output = np.sum(data["02-ribbon"])
print(output)

aocutils.outputToTextFile(data)