import sys
sys.path.append('..')
import aocutils
from collections import deque

data = {}
data["00-raw"] = aocutils.listLines(day="07", part="2")
dataLength = len(data["00-raw"])

data["01-varStorage"] = {}
data["02-split"] = [[x.split(" ") for x in line.split(" -> ")][::-1] for line in data["00-raw"]]

instructionQueue = deque(data["02-split"])

def getVariable(variable) -> int:
    try:
        return data["01-varStorage"][variable]
    except KeyError:
        try:
            return int(variable)
        except ValueError:
            return -1

def setVariable(variable, instruction) -> bool:
    value = parseInstruction(instruction)
    
    if value < 0:
        return False
    
    # Force override without modifying input
    if variable == 'b':
        value = 46065

    data["01-varStorage"][variable] = value
    return True
    

def parseInstruction(instruction) -> int:
    match len(instruction):
        case 1:
            try:
                return int(instruction[0])
            except ValueError:
                return getVariable(instruction[0])

        case 2:
            first = getVariable(instruction[1])
            
            if first < 0:
                return -1
            
            return (~first) % 65536
        
        case 3:
            first = getVariable(instruction[0])
            second = getVariable(instruction[2])

            if first < 0 or second < 0:
                return -1
            
            match instruction[1]:
                case 'AND':
                    return (first & second) % 65536
                case 'OR':
                    return (first | second) % 65536
                case 'LSHIFT':
                    return (first << second) % 65536
                case 'RSHIFT':
                    return (first >> second) % 65536
                
while len(instructionQueue):
    currentLine = instructionQueue.popleft()
    success = setVariable(currentLine[0][0], currentLine[1])
    if not success:
        instructionQueue.append(currentLine)

output = getVariable('a')
print(output)

# 46880 (too high)

aocutils.outputToTextFile(data)