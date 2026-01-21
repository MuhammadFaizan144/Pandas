#df.sort_values(by=["column_name1","column_name2"],ascending=True|False,inplace=True|False)
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'Salary': [10000,20000,30000,40000],
    "Performance_Score": [88, 92, 85, 95]
}
df=pd.DataFrame(data)
df.sort_values(by=["Age","Salary"], ascending=[True, False], inplace=True)
print(df)