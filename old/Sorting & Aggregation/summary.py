# df["Column_Name"].sum() # it will give sum of all values in that column
# df["Column_Name"].mean() # it will give mean of all values in that column
# df["Column_Name"].max() # it will give maximum value in that column
# df["Column_Name"].min() # it will give minimum value in that column
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Eva'],
    'Age': [24, 30, 22, 35],
    'Salary': [10000,20000,30000,40000],
    "Performance_Score": [88, 92, 85, 95]
}
df=pd.DataFrame(data)
avg_salary=df["Salary"].mean()
print("Average Salary:",avg_salary)