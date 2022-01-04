import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

cols = [2]
df = pd.read_excel('python_genesis/python_genesis/data_visualiztion/testData.xlsx', index_col='number')
df2 = pd.DataFrame()

df2 = df2.append(df[df['average'] > 80])

for i in [5, 10]:
    sb.histplot(data=df2, x= 'average', kde=True, bins= i)

plt.show()
