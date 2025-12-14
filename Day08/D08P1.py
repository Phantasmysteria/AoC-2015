import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="08", part="1")
dataLength = len(data["00-raw"])

# Order matters...
data["01-backslashToHash"] = [re.sub("\\\\", "#", line)[1:-1] for line in data["00-raw"]]
data["02-doubleHashToExclamation"] = [re.sub("##", "!", line) for line in data["01-backslashToHash"]]
data["03-escapeBackslash"] = [re.sub('#"', "@", line) for line in data["02-doubleHashToExclamation"]]
data["04-hex"] = [re.sub('#x[0-9a-f][0-9a-f]', "$", line) for line in data["03-escapeBackslash"]]
data["05-charDifferences"] = [len(data["00-raw"][i]) - len(data["04-hex"][i]) for i in range(dataLength)]

output = sum(data["05-charDifferences"])
print(output)

aocutils.outputToTextFile(data)