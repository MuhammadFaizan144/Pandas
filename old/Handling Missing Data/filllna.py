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

# df.fillna(0,inplace=True)#it will fill all missing values with 0
# df['Age'].fillna(df['Age'].mean(),inplace=True) # fill missing values in 'Age' column with mean of that column
df['Salary'].fillna(df['Salary'].mean(),inplace=True) # fill missing values in 'Salary' column with median of that column
print(df)