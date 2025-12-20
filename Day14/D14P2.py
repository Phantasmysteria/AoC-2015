import sys
sys.path.append('..')
import aocutils
import re
import numpy as np
import math

data = {}
data["00-raw"] = aocutils.listLines(day="14", part="2")
dataLength = len(data["00-raw"])

# Well, also some numpy...
parsePattern = "([a-zA-Z]+) can fly (\\d+) km/s for (\\d+) seconds, but then must rest for (\\d+) seconds."

elapsedTime = 2503

data["01-parsed"] = [re.search(parsePattern, item) for item in data["00-raw"]]
data["01-parsed"] = [(item.group(1), int(item.group(2)), int(item.group(3)), int(item.group(4))) for item in data["01-parsed"]]

data["02-distancesPerSecond"] = np.array([[math.floor(i / (travelTime + restTime)) * (speed * travelTime) + speed * min((i % (travelTime + restTime)), travelTime) for i in range(1, elapsedTime+1)] for name, speed, travelTime, restTime in data["01-parsed"]]).T

data["03-pointsPerSecond"] = np.apply_along_axis(lambda x: x == np.max(x), arr=data["02-distancesPerSecond"], axis=1).astype(int)
data["04-pointsTotal"] = np.sum(data["03-pointsPerSecond"], axis=0)

# Of course, of course Rudolph won...
output = np.max(data["04-pointsTotal"])
print(output)

aocutils.outputToTextFile(data)