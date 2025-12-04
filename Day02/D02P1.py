import sys
sys.path.append('..')
import aocutils
import math
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="02", part="1")
dataLength = len(data["00-raw"])

data["01-sides"] = np.array([[int(x) for x in item.split("x")] for item in data["00-raw"]])
# now this is some quality math equation
data["02-wrappingPaper"] = np.apply_along_axis(lambda arr: np.square(np.sum(arr)) - np.sum(np.square(arr)) + np.prod(arr) // np.amax(arr), axis=1, arr=data["01-sides"])

output = np.sum(data["02-wrappingPaper"])
print(output)

aocutils.outputToTextFile(data)