import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("new_deaths.csv")

plt.boxplot(data.World)
plt.title("Box Plot of World New Deaths")
plt.ylabel("New Deaths")
plt.show()
