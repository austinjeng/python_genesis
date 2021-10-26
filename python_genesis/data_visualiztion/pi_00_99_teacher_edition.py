from sympy import *

piString =  str(pi.evalf(1001))[2:]

digit = set()
for i in range(100):
    digit.add((str(i).zfill(2)))

s1 = set()
L = []
i = 0
count = 0
while s1 != digit:
    if piString[i: i + 2] not in s1:
        count = count + 1
        s1.add(piString[i: i + 2])
        L.append((count, i + 1))
    i = i + 1

print(L)

#[(第幾個找到的, 在哪裡找到的), (), ()......()] 