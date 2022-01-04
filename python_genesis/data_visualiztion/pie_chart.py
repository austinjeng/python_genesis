import matplotlib.pyplot as plt


labels = 'Science', 'Law', 'Business','Foreign', 'Big data', 'Social'
sizes = [500, 1000, 3000, 1500, 250, 2000]
explode = (0, 0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Title')
plt.show()