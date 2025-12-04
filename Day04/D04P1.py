import sys
sys.path.append('..')
import aocutils
import hashlib

data = {}
data["00-raw"] = aocutils.listLines(day="04", part="1")
dataLength = len(data["00-raw"])

# really?

i = 0
combinedHash = ""
while not combinedHash.startswith("00000"):
    combinedHash = hashlib.md5(f"{data['00-raw'][0]}{str(i)}".encode()).hexdigest()
    i += 1

output = i - 1
print(output)

aocutils.outputToTextFile(data)