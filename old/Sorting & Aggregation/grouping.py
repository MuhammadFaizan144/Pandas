
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David','Eva'],
    'Age': [24, 22, 22, 28, 28],
    'Salary': [10000,20000,30000,40000,25000],
}
df=pd.DataFrame(data)
groupby=df.groupby(["Age","Name"])["Salary"].sum()
print(groupby)