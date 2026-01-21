"""
vertically (row-wise) concatenation of dataframes
pd.concat([df1,df2,df3,...],axis=0|1,ignore_index=True|False)

horizontally (column-wise) concatenation of dataframes
pd.concat([df1,df2,df3,...],axis=1,ignore_index=True|False)

axis=1 -> column-wise
axis=0 -> row-wise
ignore_index=True -> reindexing the new dataframe
"""
import pandas as pd
df_Region1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
})
df_Region2 = pd.DataFrame({
    'CustomerID': [4, 5, 6],
    'Name': ['David', 'Eva', 'Frank'],
})
# Vertical Concatenation (Row-wise)
df_concat=pd.concat([df_Region1,df_Region2],axis=0,ignore_index=True)
print("Vertical Concatenation (Row-wise):")
print(df_concat)

# Horizontal Concatenation (Column-wise)
df_concat=pd.concat([df_Region1,df_Region2],axis=1,ignore_index=False)
print("Horizontal Concatenation (Column-wise):")
print(df_concat)