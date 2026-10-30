import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'Salary': [50000, 60000, 55000, 70000],
    "Performance_Score": [88, 92, 85, 95]
}
df = pd.DataFrame(data)
print("sample data frame")
print(df)

# .loc[]
# df.loc[row_index,column name]
df['Salary']=df['Salary']*1.05
print(df)