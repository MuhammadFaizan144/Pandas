"""
1-how big is your data set?
2-what are the name of your columns?

shape and column
"""
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'Salary': [50000, 60000, 55000, 70000],
    "Performance_Score": [88, 92, 85, 95]
}
df = pd.DataFrame(data)
print(df)
print(f'shape:{df.shape}')  # Output: shape:(4, 4)
print(f'columns:{df.columns}')  # Output: columns:['Name', 'Age', 'Salary', 'Performance_Score']