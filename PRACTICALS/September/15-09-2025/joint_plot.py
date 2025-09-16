import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("dark")
tips=sns.load_dataset('tips')
sns.jointplot(x='total_bill', y='tip',data=tips)

sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')

sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex') 

