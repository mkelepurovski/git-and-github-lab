import pandas as pd
df=pd.read_csv("C:/Users/mkele/Downloads/sales.csv")
print("N rows:", len(df))
print("Mean sale:", df["amount"].mean())
print("Largest sale:", df["amount"].max())
