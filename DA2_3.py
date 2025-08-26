import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("new_deaths.csv")

x = data["date"]
y = data["United States"]

plt.bar(x, y, color = "blue")
plt.title("New Deaths in United States")
plt.xlabel("Date")
plt.ylabel("Total")
plt.show()