import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="05", part="2")
dataLength = len(data["00-raw"])

data["01-duplicateGroupCheck"] = list(filter(lambda x: re.search("(..).*\\1", x), data["00-raw"]))
data["02-sandwichCheck"] = list(filter(lambda x: re.search("(.).\\1", x), data["01-duplicateGroupCheck"]))

output = len(data["02-sandwichCheck"])
print(output)

aocutils.outputToTextFile(data)