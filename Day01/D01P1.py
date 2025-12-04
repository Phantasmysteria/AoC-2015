import sys
sys.path.append('..')
import aocutils
import math
import numpy as np
from functools import reduce

data = {}
data["00-raw"] = aocutils.listLines(day="01", part="1")
dataLength = len(data["00-raw"])

output = sum(list(map(lambda x: 1 if x == '(' else -1, data["00-raw"][0])))
print(output)

aocutils.outputToTextFile(data)