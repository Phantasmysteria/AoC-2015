import sys
sys.path.append('..')
import aocutils
import math
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="03", part="2")
dataLength = len(data["00-raw"])

data["01-visitedPresents"] = {
    (0, 0): 1
}
currentLocation = [(0, 0), (0, 0)]

for i in range(len(data["00-raw"][0])):
    dir = data["00-raw"][0][i]
    currentLocation[i % 2] = (currentLocation[i % 2][0] + (dir == ">") - (dir == "<"), currentLocation[i % 2][1] + (dir == "^") - (dir == "v"))
    if currentLocation[i % 2] not in data["01-visitedPresents"]:
        data["01-visitedPresents"][currentLocation[i % 2]] = 0
    data["01-visitedPresents"][currentLocation[i % 2]] += 1

output = len(data["01-visitedPresents"].keys())
print(output)

aocutils.outputToTextFile(data)