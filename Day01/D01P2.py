import sys
sys.path.append('..')
import aocutils
import math
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="01", part="2")
dataLength = len(data["00-raw"])

output = 0
count = 0
for c in data["00-raw"][0]:
    output += 1
    count += 1 if c == '(' else -1
    if count < 0:
        break
print(output)

aocutils.outputToTextFile(data)