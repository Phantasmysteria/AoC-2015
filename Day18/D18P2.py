import sys
sys.path.append('..')
import aocutils
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="18", part="1")
dataLength = len(data["00-raw"])

data["01-grid"] = aocutils.TwoDGrid(np.array([[c == '#' for c in item] for item in data["00-raw"]], dtype=int), False)
for corner in data["01-grid"].corners():
    data["01-grid"].grid[corner] = 1

# Conway's GIF of Life lmao
for iteration in range(100):
    for y, x in data["01-grid"].allIndices():
        surroundOn = data["01-grid"].eightNeighboursSum(y, x, False)
        if data["01-grid"].grid[y, x]:
            data["01-grid"].stageGrid[y, x] = (surroundOn == 2 or surroundOn == 3)
        else:
            data["01-grid"].stageGrid[y, x] = (surroundOn == 3)

    data["01-grid"].commit()
    for corner in data["01-grid"].corners():
        data["01-grid"].grid[corner] = 1

output = np.sum(data["01-grid"].grid)
print(output)

# 922 (too low)

aocutils.outputToTextFile(data)