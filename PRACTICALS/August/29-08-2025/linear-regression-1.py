import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from pandas.core.common import random_state
from sklearn.linear_model import LinearRegression

df = pd.read_csv("PRACTICALS\\August\\29-08-2025\\Study_vs_Score_data.csv" , encoding='latin-1')
df.head()
df.info()
print(df.describe())

# plt.scatter(df['Attendance_Hours'], df['Final_Marks'], color = 'purple')
# plt.title('Attendance Hours vs Final Marks')
# plt.xlabel('Attendance Hours')
# plt.ylabel('Final Marks')
# plt.box(False)
# plt.show()

X = df[['Attendance_Hours']]
y = df['Final_Marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred_test = regressor.predict(X)     # predicted value of y_test
y_pred_train = regressor.predict(X_train)   # predicted value of y_train

plt.scatter(X_train, y_train, color = 'lightcoral')
plt.plot(X_train, y_pred_train, color = 'firebrick')
plt.title('Attendance_Hours vs Final_Marks (Training Set)')
plt.xlabel('Attendance_Hours')
plt.ylabel('Final_Marks')
plt.legend(['X_train/Pred(y_test)', 'X_train/y_train'], title = 'Study/GPA', loc='best', facecolor='white')
plt.box(False)
plt.show()
