import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

cols = [2]
df = pd.read_excel('python_genesis/python_genesis/data_visualiztion/testData.xlsx', index_col='number')

sb.histplot(data=df, x= 'average', kde=True)
plt.show()