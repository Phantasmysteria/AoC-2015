import sys
sys.path.append('..')
import aocutils
import itertools

data = {}
data["00-raw"] = aocutils.listLines(day="17", part="1")
dataLength = len(data["00-raw"])

data["01-weights"] = sorted(list(map(int, data["00-raw"])), reverse=True)
maxWeight = 150

# from https://docs.python.org/3/library/itertools.html
def powerSetRange(num):
    s = list(range(num))
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

data["02-matchingWeights"] = set()

for combination in powerSetRange(20):
    if sum([data["01-weights"][i] for i in combination]) == maxWeight:
        data["02-matchingWeights"].add(combination)

output = len(data["02-matchingWeights"])
print(output)

aocutils.outputToTextFile(data)