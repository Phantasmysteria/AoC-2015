import sys
sys.path.append('..')
import aocutils
import re
import itertools

data = {}
data["00-raw"] = aocutils.listLines(day="13", part="1")
dataLength = len(data["00-raw"])

parsePattern = "([a-zA-Z]+) would (gain|lose) (\\d+) happiness units by sitting next to ([a-zA-Z]+)."

data["01-parsed"] = [re.search(parsePattern, item) for item in data["00-raw"]]
data["01-parsed"] = [((item.group(1), item.group(4)), int(item.group(3)) * (-1 if item.group(2) == 'lose' else 1)) for item in data["01-parsed"]]

data["02-map"] = {item[0]: item[1] for item in data["01-parsed"]}

output = 0

for seating in itertools.permutations(['Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory']):
    loopSeating = [seating[-1]] + list(seating) + [seating[0]]
    total = 0
    for i in range(1, len(seating)+1):
        total += data["02-map"][(loopSeating[i], loopSeating[i-1])] + data["02-map"][(loopSeating[i], loopSeating[i+1])]
    
    if total > output:
        output = total

print(output)

aocutils.outputToTextFile(data)