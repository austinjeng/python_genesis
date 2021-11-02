# Libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Create dataset
height = [25 ,6 ,6 ,5 ,5]
bars = ('Psychosis', 'Broken limbs', 'Herniated disc', 'Mental illness', 'Severe depression')
x_pos = np.arange(len(bars))
 
# Create bars
plt.bar(x_pos, height)
 
# Create names on the x-axis
plt.xticks(x_pos, bars)
 
# Show graphic
plt.show()