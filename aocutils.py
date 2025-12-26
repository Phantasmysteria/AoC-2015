from typing import List, Any
import itertools
import pprint
import numpy as np

# Quick way to convert input file into list of lines
def listLines(day: str, part: str) -> List[str]:
    with open(f"inputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt", "r") as f:
        return [item.rstrip() for item in f.readlines()]

# Quick way to convert input file into list of lines (without removing end spaces)
def listLinesWithSpaces(day: str, part: str) -> List[str]:
    with open(f"inputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt", "r") as f:
        return [item[:-1] if item[-1] == '\n' else item for item in f.readlines()]

# Quick way to convert input file into list of list of lines separated by delimiter
def listLinesWithGroup(day: str, part: str, groupSep: str) -> List[str]:
    with open(f"inputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt", "r") as f:
        return [list(group) for key, group in itertools.groupby([item.rstrip() for item in f.readlines()], lambda x: x == groupSep) if not key]

# Output pretty print to text file, remove default Nones when reused in new repo
def outputToTextFile(data: Any, day: str = None, part: str = None) -> None:
    filename = "output.txt" if (day is None and part is None) else f"outputD{day}Ex.txt" if part == "ex" else f"inputD{day}P{part}.txt"
    with open(filename, "w") as f:
        f.write(pprint.pformat(data))

# Get slice of dict from [start, end]
def sliceView(data: dict, start: int, end: int) -> dict:
    ret = {}
    for k, v in data.items:
        try:
            ret[k] = v[start:end+1]
        except (TypeError, IndexError):
            ret[k] = v
    return ret

# Yes I know Counter class exists
def addToCounter(data: dict[Any, int], key: Any, val: int) -> None:
    if key not in data:
        data[key] = 0
    data[key] += val

# Variant of hash map with lists as values
def addToBucket(data: dict[Any, list[Any]], key: Any, val: Any) -> None:
    if key not in data:
        data[key] = []
    data[key].append(val)

# I have never implemented union-find until now
class UnionFindSize:
    def __init__(self, length):
        self.parents = list(range(length))
        self.sizes = [1 for _ in range(length)]

    def find(self, x):
        if self.parents[x] == x:
            return self.parents[x]
        return self.find(self.parents[x])

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return

        if self.sizes[xRoot] < self.sizes[yRoot]:
            xRoot, yRoot = yRoot, xRoot

        self.parents[yRoot] = xRoot
        self.sizes[xRoot] += self.sizes[yRoot]

    def __repr__(self):
        return str([(x, y) for x, y in zip(self.parents, self.sizes)])

# Finally decided to write a 2D grid class
class TwoDGrid:
    def __init__(self, grid, wrap):
        self.grid = np.copy(grid)
        self.height, self.width = grid.shape
        self.wrap = wrap
        self.stageGrid = np.copy(grid)

    def allIndices(self):
        return np.ndindex(self.height, self.width)
    
    def corners(self):
        return [(0, 0), (0, self.width-1), (self.height-1, 0), (self.height-1, self.width-1)]

    def commit(self):
        self.grid = np.copy(self.stageGrid)

    def shift(self, y0, x0, y1, x1):
        if (y1 == 0 and x1 == 0):
            return None
        
        y = y0 + y1
        x = x0 + x1

        if self.wrap:
            return (y % self.height, x % self.width)
        
        if not self.wrap and (y < 0 or x < 0 or y >= self.height or x >= self.width):
            return None
    
        return (y, x)

    def eightNeighboursIndices(self, y, x):
        return [item for item in [self.shift(y, x, *coords) for coords in itertools.product([-1, 0, 1], [-1, 0, 1])] if item is not None]

    def eightNeighboursValues(self, y, x):
        return [self.grid[item] for item in self.eightNeighboursIndices(y, x)]

    def eightNeighboursSum(self, y, x, includeSelf):
        return sum(self.eightNeighboursValues(y, x)) + (includeSelf * self.grid[y, x])

    def __repr__(self):
        return f"2DGrid({self.height, self.width}, {self.wrap},\n\n{self.grid},\n\n{self.stageGrid})"

if __name__ == '__main__':
    print("Why are you running this file?")