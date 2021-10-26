from math import pi
from sympy import *
# Hello 
piString = pi.evalf(201)
piString = str(piString)
piString = piString[2:]

digit = set()

for i in range(10):
    digit.add(str(i))

L = set()
i = 0

while digit != L:
    if piString[i] not in L:
        L.add(piString[i])
        print(sorted(L), i)

    i += 1

L = sorted(L)
print(L)
