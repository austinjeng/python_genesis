import csv
import pandas as pd
from pandas import read_csv
from matplotlib import pyplot as plt
import seaborn as sb
import numpy as np

csv_data = read_csv("/Users/austin/VS_Code/python_genesis/python_genesis/data_visualiztion/2021-tainan-pop-proj.csv")
sb.histplot(csv_data['test'], kde = False)
plt.show()
        
