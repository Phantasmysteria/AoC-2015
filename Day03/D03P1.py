import sys
sys.path.append('..')
import aocutils
import math
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="03", part="1")
dataLength = len(data["00-raw"])

# i predicted part 2 would ask how many presents in total but i was wrong
data["01-visitedPresents"] = {
    (0, 0): 1
}
currentLocation = (0, 0)

for dir in data["00-raw"][0]:
    currentLocation = (currentLocation[0] + (dir == ">") - (dir == "<"), currentLocation[1] + (dir == "^") - (dir == "v"))
    if currentLocation not in data["01-visitedPresents"]:
        data["01-visitedPresents"][currentLocation] = 0
    data["01-visitedPresents"][currentLocation] += 1

output = len(data["01-visitedPresents"].keys())
print(output)

aocutils.outputToTextFile(data)