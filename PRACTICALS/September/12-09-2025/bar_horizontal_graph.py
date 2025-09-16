import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\admin\\Downloads\\Coffe_sales.csv")

coffee_types = df["coffee_name"].unique()
coffee_totals = [df[df["coffee_name"] == c]["money"].sum() for c in coffee_types]

plt.barh(coffee_types, coffee_totals, color="skyblue")
plt.title("Total Sales by Coffee Type")
plt.xlabel("Coffee Type")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()
