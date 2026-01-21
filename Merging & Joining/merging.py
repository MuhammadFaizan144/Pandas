#pd.merge(datafame1,dataframe2, on="column_name",how="type of join inner|outer|left|right")

import pandas as pd
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 6],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Amount': [250, 150, 300, 400]
})

df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how="inner")
print("Inner Join:")
print(df_merged)

df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how="outer")
print("Outer Join:")
print(df_merged)


df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how="left")
print("Left Join:")
print(df_merged)


df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how="right")
print("Right Join:")
print(df_merged)


df_merged=pd.merge(df_customers,df_orders,on="CustomerID",how="cross")
print("Cross Join:")
print(df_merged)