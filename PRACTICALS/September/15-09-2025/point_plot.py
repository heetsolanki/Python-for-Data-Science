# importing required packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
   
# loading dataset 
data = sns.load_dataset("tips") 
sns.pointplot(x="day", y="tip", data=data)
plt.show()

sns.pointplot(x="time", y="total_bill", hue="smoker",
                   data=data, palette="Accent")
plt.show()