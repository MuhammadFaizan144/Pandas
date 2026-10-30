#head() tail()
#head(n=5)  #first n rows
#head()  #first 5 rows by default
#tail(n=5)  #last n rows
#tail()  #last 5 rows by default
import pandas as pd
df=pd.read_json("sample_Data.json")
print("Displaying first 10 rows:")
print(df.head())
print("Displaying last 10 rows:")
print(df.tail())