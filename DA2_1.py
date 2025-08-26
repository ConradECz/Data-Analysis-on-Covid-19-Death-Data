import pandas as pd

data = pd.read_csv("new_deaths.csv")

print(data.World.describe())