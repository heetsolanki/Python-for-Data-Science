# importing required packages 
import seaborn as sns 
import matplotlib.pyplot as plt 
   
# loading dataset 
data = sns.load_dataset("tips") 
sns.pointplot(x="day", y="tip", data=data)
plt.show()
