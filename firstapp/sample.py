import pandas as pd

samp = pd.read_csv("/mnt/c/Users/Vasanth/fastapi/firstapp/organizations-100.csv")
df = samp.dropna()
print("dataframe",df)

