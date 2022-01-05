import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = pd.read_excel('python_genesis/python_genesis/data_visualiztion/testData.xlsx', index_col='number')

sb.boxplot(data=df, x= 'view by', y = 'average')

plt.show()
