import pandas as pd
data = {
    'Name': ['Alice', None, 'Charlie', 'David'],
    'Age': [24, None, 22, 35],
    'Salary': [50000, None, 55000, 70000],
    "Performance_Score": [88, None, 85, 95]
}
df = pd.DataFrame(data)
print("sample data frame")
print(df)
# dropna() to remove rows with missing values
# df.dropna(axis=0,inplace=True)
df.dropna(inplace=True)
print(df)