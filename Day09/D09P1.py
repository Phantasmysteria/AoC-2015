import sys
sys.path.append('..')
import aocutils
import re
from collections import deque

data = {}
data["00-raw"] = aocutils.listLines(day="09", part="1")
dataLength = len(data["00-raw"])

data["01"] = [re.search("(\\w*) to (\\w*) = (\\d*)", line) for line in data["00-raw"]]
data["02-adjList"] = {}

for pair in data["01"]:
    src, dest, weight = pair.group(1), pair.group(2), int(pair.group(3))
    if src not in data["02-adjList"]:
        data["02-adjList"][src] = []
    if dest not in data["02-adjList"]:
        data["02-adjList"][dest] = []
    data["02-adjList"][src].append((dest, weight))
    data["02-adjList"][dest].append((src, weight))

data["03-completePaths"] = []

queue = deque((0, (loc,)) for loc in data["02-adjList"].keys())

while len(queue):
    cost, locPath = queue.popleft()

    if len(locPath) == len(data["02-adjList"].keys()):
        data["03-completePaths"].append((cost, locPath))
        continue
    
    queue.extend([(cost + nCost, (*locPath, neighbour)) for neighbour, nCost in data["02-adjList"][locPath[-1]] if neighbour not in locPath])    

data["04"] = sorted(data["03-completePaths"], key=lambda x: x[0])

output = data["04"][0][0]
print(output)

aocutils.outputToTextFile(data)