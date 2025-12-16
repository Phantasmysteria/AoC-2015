import sys
sys.path.append('..')
import aocutils
import itertools

data = {}
data["00-raw"] = aocutils.listLines(day="10", part="1")
dataLength = len(data["00-raw"])

# Ah, it's look and say sequence
data["01-sequences"] = [data["00-raw"][0]]

for i in range(50):
    data["01-sequences"].append("".join([str(len(list(v))) + k for k, v in itertools.groupby(data["01-sequences"][-1])]))

output = len(data["01-sequences"][-1])
print(output)

aocutils.outputToTextFile(data)