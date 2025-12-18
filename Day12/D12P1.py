import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="12", part="1")
dataLength = len(data["00-raw"])

data["01-numbers"] = list(map(int, re.findall("-*\\d+", data["00-raw"][0])))

output = sum(data["01-numbers"])
print(output)

aocutils.outputToTextFile(data)