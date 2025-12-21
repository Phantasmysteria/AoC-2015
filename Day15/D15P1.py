import sys
sys.path.append('..')
import aocutils
import re
import numpy as np

data = {}
data["00-raw"] = aocutils.listLines(day="15", part="1")
dataLength = len(data["00-raw"])

parsePattern = "([a-zA-Z]+): capacity (-*\\d+), durability (-*\\d+), flavor (-*\\d+), texture (-*\\d+), calories (-*\\d+)"

data["01-parsed"] = [re.search(parsePattern, item) for item in data["00-raw"]]
data["01-parsed"] = np.array([[int(item.group(2)), int(item.group(3)), int(item.group(4)), int(item.group(5))] for item in data["01-parsed"]])

totalTeaspoons = 100
numIngredients = 4

def combinations(numMax, numBins):
    if numBins <= 1:
        yield [numMax]
    else:
        for i in range(numMax + 1):
            for bins in combinations(numMax - i, numBins - 1):
                yield [i] + bins

data["02-properties"] = data["01-parsed"].T[:, np.newaxis, :]

data["03-combinations"] = np.array(list(combinations(totalTeaspoons, numIngredients)))

# want: (total, ingr) x (prop, [1], ingr) => (prop, total, ingr)
data["04-propertyMulti"] = data["03-combinations"] * data["02-properties"]

# want: (prop, total, ingr) => (prop, total) => (total, )
data["05-propertySums"] = np.sum(data["04-propertyMulti"], axis=2)
data["05-propertySums"] = np.maximum(data["05-propertySums"], np.zeros_like(data["05-propertySums"]))

data["06-scores"] = np.prod(data["05-propertySums"], axis=0)

output = np.max(data["06-scores"])
print(output)

aocutils.outputToTextFile(data)