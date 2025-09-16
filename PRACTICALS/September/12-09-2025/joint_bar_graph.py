import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\admin\\Downloads\\Coffe_sales.csv")

coffee_types = df["coffee_name"].unique()
coffee_totals = [df[df["coffee_name"] == c]["money"].sum() for c in coffee_types]

colors = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3"]

bar_width = 0.2
x = range(len(coffee_types))

for i, t in enumerate(time_types):
    values = [df[(df["coffee_name"] == c) & (df["Time_of_Day"] == t)]["money"].sum() for c in coffee_types]
    plt.bar([p + i*bar_width for p in x], values, width=bar_width, label=t)

plt.title("Grouped Bar Chart: Coffee Sales by Time of Day")
plt.xlabel("Coffee Type")
plt.ylabel("Total Sales")
plt.xticks([p + bar_width for p in x], coffee_types, rotation=45)
plt.legend()
plt.show()