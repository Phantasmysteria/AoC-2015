import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="14", part="1")
dataLength = len(data["00-raw"])

# So the early AoC puzzles are mosly input parsing?
parsePattern = "([a-zA-Z]+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds."

elapsedTime = 2503

data["01-parsed"] = [re.search(parsePattern, item) for item in data["00-raw"]]
data["01-parsed"] = [(item.group(1), int(item.group(2)), x := int(item.group(3)), y := int(item.group(4)), *divmod(elapsedTime, x+y)) for item in data["01-parsed"]]

data["02-distances"] = [(name, 
                         laps * (speed * travelTime) + speed * min(remainder, travelTime)
                         ) for name, speed, travelTime, restTime, laps, remainder in data["01-parsed"]]

data["02-distances"] = sorted(data["02-distances"], key=lambda x: x[1], reverse=True)

output = data["02-distances"][0][1]
print(output)

aocutils.outputToTextFile(data)