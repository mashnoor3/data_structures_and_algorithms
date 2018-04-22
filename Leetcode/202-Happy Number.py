from collections import defaultdict
import math

def isHappy(n):
    l = splitNumber(n)
    sum = 0
    mem = set()
    while True:
        for i in l:
            sum += int(math.pow(i,2))
        if sum in mem:
            return False
        elif sum == 1:
            return True
        else:
            mem.add(sum)
            l = splitNumber(sum)
            sum = 0

def splitNumber(n):
    quot, rem, output = n, 0, []
    while quot != 0:
        rem = quot % 10
        quot = quot // 10
        output.append(rem)
    return output

isHappy(1931)
isHappy(19)
