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
# df.drop(columns=['Method name'], inplace=True)
df.drop(columns=['Performance_Score','Age'], inplace=True)
print("data frame after removing column")
print(df)