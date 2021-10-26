from math import pi
from sympy import *

piString = pi.evalf(10001)
piString = str(piString)
piString = piString[2:]

setOf0To99 = set()


for i in range(0, 100, 11):
    setOf0To99.add((str(i).zfill(2)))



L = set()
i = 0

while setOf0To99 != L:
    if piString[i: i+2] in setOf0To99 not in L:
        #print(piString[i])
        L.add(piString[i : i+2])
        print(sorted(L), i)
        
    i += 2

