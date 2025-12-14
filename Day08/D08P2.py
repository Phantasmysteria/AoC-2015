import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="08", part="2")
dataLength = len(data["00-raw"])

# Easier than part 1
data["01-backslashToHash"] = [re.sub("\\\\", "##", line) for line in data["00-raw"]]
data["02-expandDoubleQuote"] = [re.sub('"', '#"', line) for line in data["01-backslashToHash"]]
data["03-charDifferences"] = [len(data["02-expandDoubleQuote"][i]) - len(data["00-raw"][i]) + 2 for i in range(dataLength)]

output = sum(data["03-charDifferences"])
print(output)

aocutils.outputToTextFile(data)