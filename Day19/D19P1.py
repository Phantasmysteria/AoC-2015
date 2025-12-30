import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="19", part="1")
dataLength = len(data["00-raw"])

data["01-matches"] = [re.search(f"(\\w+) => (\\w+)", item) for item in data["00-raw"][:-2]]
data["02-replacements"] = {}

for m in data["01-matches"]:
    aocutils.addToBucket(data["02-replacements"], m.group(1), m.group(2))

data["03-uniques"] = set()
moleculeString = data["00-raw"][-1]

for rep in data["02-replacements"].keys():
    for m in re.finditer(rep, moleculeString):
        for r in data["02-replacements"][rep]:
            data["03-uniques"].add(moleculeString[:m.start()] + r + moleculeString[m.end():])

output = len(data["03-uniques"])
print(output)

aocutils.outputToTextFile(data)