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

# adding new column
df["Bonus"]=df["Salary"]*0.1
print(df)
# using insert
df.insert(0,"Employee_ID",[101,102,103,104])
print(df)