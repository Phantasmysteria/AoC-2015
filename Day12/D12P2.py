import sys
sys.path.append('..')
import aocutils
import re
import json

data = {}
data["00-raw"] = aocutils.listLines(day="12", part="2")
dataLength = len(data["00-raw"])

data["01-json"] = json.loads(data["00-raw"][0])

def traverse(obj):
    totalSum = 0
    
    if isinstance(obj, int):
        totalSum += obj
    
    if isinstance(obj, list):
        for item in obj:
            totalSum += traverse(item)
    
    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        for item in obj.values():
            totalSum += traverse(item)

    return totalSum

output = traverse(data["01-json"])
print(output)

aocutils.outputToTextFile(data)