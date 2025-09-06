import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# from pandas.core.common import random_state
# from sklearn.linear_model import LinearRegression

df = pd.read_csv("PRACTICALS\\August\\29-08-2025\\Study_vs_Score_data.csv" , encoding='latin-1')
df.head()


from matplotlib import pyplot as plt
df.plot(kind='scatter', x='Attendance_Hours', y='Final_Marks', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()
