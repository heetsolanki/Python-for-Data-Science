import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\admin\\Downloads\\Coffe_sales.csv")

coffee_types = df["coffee_name"].unique()
coffee_totals = [df[df["coffee_name"] == c]["money"].sum() for c in coffee_types]

time_types = df["Time_of_Day"].unique()
stack_data = {t: [df[(df["coffee_name"] == c) & (df["Time_of_Day"] == t)]["money"].sum() for c in coffee_types] for t in time_types}

colors = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3"]

bar_width = 0.5
bottom = [0]*len(coffee_types)

for idx, t in enumerate(time_types):
    plt.bar(coffee_types, stack_data[t], bottom=bottom, label=t, color=colors[idx % len(colors)])
    bottom = [i+j for i,j in zip(bottom, stack_data[t])]

plt.title("Stacked Bar Chart: Coffee Sales by Time of Day")
plt.xlabel("Coffee Type")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.legend(title="Time of Day")
plt.show()
