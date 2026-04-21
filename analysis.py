import pandas as pd

df = pd.read_csv("data.csv")

print("Dataset:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())