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

data["03-matchingWeightsMin"] = [item for item in data["02-matchingWeights"] if len(item) == min([len(i) for i in data["02-matchingWeights"]])]

output = len(data["03-matchingWeightsMin"])
print(output)

aocutils.outputToTextFile(data)