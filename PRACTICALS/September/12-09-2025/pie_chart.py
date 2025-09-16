import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\admin\\Downloads\\Coffe_sales.csv")

coffee_types = df["coffee_name"].unique()
coffee_totals = [df[df["coffee_name"] == c]["money"].sum() for c in coffee_types]

plt.pie(coffee_totals, labels=coffee_types, autopct='%1.1f%%')
plt.title("Total Sales by Coffee Type (Pie Chart)")
plt.show()
