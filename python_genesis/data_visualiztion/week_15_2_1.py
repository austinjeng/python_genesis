import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = pd.read_excel('python_genesis/python_genesis/data_visualiztion/testData.xlsx', index_col='number')
df2 = pd.DataFrame()

df2 = df2.append(df[df['average'] > 80])

sb.jointplot(data=df2, x= 'data review', y = 'interview')

plt.show()
