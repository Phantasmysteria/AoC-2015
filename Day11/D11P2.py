import sys
sys.path.append('..')
import aocutils
import re

data = {}
data["00-raw"] = aocutils.listLines(day="11", part="2")
dataLength = len(data["00-raw"])

data["01-prevPassword"] = data["00-raw"][0]

def incrementString(s):
    ret = [c for c in s]
    carry = True
    index = 7
    while carry:
        if ret[index] == 'z':
            ret[index] = 'a'
            carry = True
        else:
            ret[index] = chr(ord(ret[index]) + 1)
            carry = False
        index -= 1
    return "".join(ret)

def checkValid(s):
    if re.search("[ilo]", s):
        return False
    if re.search("abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz", s):
        if re.search("(\\w)\\1.*(\\w)\\2", s):
            return True
    return False
    
# increment to find the next one
output = incrementString(data["01-prevPassword"])

while not checkValid(output):
    output = incrementString(output)
    
print(output)

aocutils.outputToTextFile(data)