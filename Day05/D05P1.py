import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="05", part="1")
dataLength = len(data["00-raw"])

data["01-vowelCheck"] = list(filter(lambda x: re.search("[aeiou].*[aeiou].*[aeiou]", x), data["00-raw"]))
data["02-duplicateCheck"] = list(filter(lambda x: re.search("(\\w)\\1", x), data["01-vowelCheck"]))
data["03-digramCheck"] = list(filter(lambda x: re.search("(ab|cd|pq|xy)", x) is None, data["02-duplicateCheck"]))

output = len(data["03-digramCheck"])
print(output)

aocutils.outputToTextFile(data)