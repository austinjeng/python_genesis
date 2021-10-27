L = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# n = 123456789 abcdefghi
max = 123456789
min = 987654321
flag = False
for a in L:
    for b in L - {a}:
        for c in L - {a} - {b}:
            for d in L - {a} - {b} - {c}:
                for e in L - {a} - {b} - {c} - {d}:
                    for f in L - {a} - {b} - {c} - {d} - {e}:
                        for g in L - {a} - {b} - {c} - {d} - {e} - {f}:
                            for h in L - {a} - {b} - {c} - {d} - {e} - {f} - {g}:
                                for i in L - {a} - {b} - {c} - {d} - {e} - {f} - {g} - {h}:
                                    n = a * 10**8 + b * 10** 7 + c * 10**6 + d * 10**5 + e * 10**4 + f * 10**3 + g * 10 ** 2 + h * 10 ** 1 + i
                                    if n % 11 == 0:
                                        #print(n)
                                        if max < n:
                                            max, n = n, max
                                            flag = True
                                        if min > n:
                                            if flag:
                                                n = max
                                                min, n = n, min
                                    flag = False

print(f'maximun is {max}, and minumum is {min}.')