#sorting data
#SORTING DATA 1 COLUMN sort_values()
#df.sort_values(by='column name',ascending=True/False,inplace=True/False)
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'Salary': [50000, 60000, 55000, 70000],
    "Performance_Score": [88, 92, 85, 95]
}
df=pd.DataFrame(data)
print(df.sort_values(by='Age',ascending=True,inplace=True))  #sort by age in ascending order