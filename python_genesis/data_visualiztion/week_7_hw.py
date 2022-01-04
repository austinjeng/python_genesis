from typing import ClassVar
import matplotlib.pyplot as plt
import numpy as np
import os, csv


labels = list()
number = list()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'sea_burial.csv')) as inputFile:
    csv_data = list(csv.reader(inputFile))[slice(5)]
    for row in csv_data:
        labels.append[row[0]]
        number.append[row[1]]

print(f'labels = {labels}')
print(f'numbers = {number}')
        
#labels = np.array(['Car Light System', 'Transmission System', 'Rotation System', 'Frame System', 'Social Science', 'Machinery'])
#number = np.array([5534, 7492, 10, 11, 175])

#def reorder(L):
#    return[L[1], L[0], L[4], L[3], L[2]]

#labels = reorder(labels)
#number = reorder(number)

width = 0.35
pos = np.arange(len(number))

p1 = plt.barh(pos, number, 0.35, color = 'blue', align = 'center', alpha = 0.5), 
plt.xlabel('no. of cases')
plt.yticks(pos, labels)
plt.title('Ubike repairment category and case counts in Taipei')
plt.legend([p1], ['cases'], loc = 'lower right')
plt.show()






