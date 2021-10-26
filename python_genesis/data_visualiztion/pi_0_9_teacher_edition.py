from sympy import *

piString =  str(pi.evalf(1001))[2:]

digit = set("0123456789")
s1 = set()
L = []
i = 0

while s1 != digit:
    if piString[i] not in s1:
        s1.add(piString[i])
        L.append((len(s1), i))
    i = i + 1

print(L)