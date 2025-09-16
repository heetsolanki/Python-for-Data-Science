import seaborn as sns
tips = sns.load_dataset("tips")
ax = sns.regplot(x="total_bill", y="tip", data=tips)

sns.regplot(x="size", y="total_bill", data=tips, x_jitter=0.1)

