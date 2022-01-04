'''
References:
    https://www.youtube.com/watch?v=LlJJQyPYCKw
    https://numpy.org/doc/stable/reference/generated/numpy.array.html
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.barh.html
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html

'''



import matplotlib.pyplot as plt
import numpy as np

labelsMale = np.array(['Business(M)', 'Law(M)', 'Science(M)', 'Foreign(M)', 'Social Science(M)', 'Big data(M)'])
labelsFemale = np.array(['Business(F)', 'Law(F)', 'Science(F)', 'Foreign(F)', 'Social Science(F)', 'Big data(F)'])
male = np.array([2037, 580, 642, 452, 1120, 91])
female = np.array([2513, 716, 550, 1497, 1959, 85])

def reorder(L):
    return [L[5], L[2], L[1], L[3], L[4], L[0]]

male = reorder(male)
female = reorder(female)
labelsMale = reorder(labelsMale)
labelsFemale = reorder(labelsFemale)

pos = np.arange(len(male))
p1 = plt.barh(pos, male)
p2 = plt.barh(pos + len(male), female)

pos2 = np.arange(len(male) * 2)
plt.yticks(pos2, labelsMale + labelsFemale)

plt.show()