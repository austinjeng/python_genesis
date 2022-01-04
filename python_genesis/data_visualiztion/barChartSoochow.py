import matplotlib.pyplot as plt
import numpy as np

labels = np.array(['Business', 'Law', 'Science', 'Foreign', 'Social Science', 'Big data'])
male = np.array([2037, 580, 642, 452, 1120, 91])
female = np.array([2513, 716, 550, 1497, 1959, 85])
total = male + female

def reorder(L):
    return [L[5], L[2], L[1], L[3], L[4], L[0]]

labels = reorder(labels)
male = reorder(male)
female = reorder(female)
total = reorder(female)

width = 0.35
pos = np.arange(len(total))

p1 = plt.barh(pos - width/2.0, male, width, color = 'blue', align = 'center', alpha = 0.5)
p2 = plt.barh(pos + width/2.0, female, width, color = 'red', align = 'center', alpha = 0.5)
plt.xlabel('Number of Students')
plt.yticks(pos, labels)
plt.title('Demographics -- Soochow University')
#plt.show()