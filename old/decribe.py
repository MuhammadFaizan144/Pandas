#step-1 sample data frame
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'Salary': [50000, 60000, 55000, 70000],
    "Performance_Score": [88, 92, 85, 95]
}
df = pd.DataFrame(data)
print(df)
print('descriptive statistics:')
print(df.describe())
# Output:
# descriptive statistics:
#              Age        Salary  Performance_Score
# count   4.000000      4.000000           4.000000
# mean   27.750000  58750.000000          90.000000
# std     5.909033   8539.125638           4.396969
# min    22.000000  50000.000000          85.000000
# 25%    23.500000  53750.000000          87.250000
# 50%    27.000000  57500.000000          90.000000
# 75%    31.250000  62500.000000          92.750000
# max    35.000000  70000.000000          95.000000