import pandas as pd
df=pd.read_csv("C:/Users/mkele/Downloads/sales.csv")
print("Number of Rows:", len(df))
print("Mean sale amount:", df["amount"].mean())