import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'Salary': [50000, 60000, 55000, 70000],
    "Performance_Score": [88, 92, 85, 95]
}
df = pd.DataFrame(data)
high_salary_df = df[df['Salary'] > 55000]
print("Employees with Salary greater than 55000:")
print(high_salary_df)

# filtering rows salary >55000 & age>30
filtered=df[(df['Age']>30)&(df['Salary']>55000)]
print("Employees with Salary greater than 55000 and Age greater than 30:")
print(filtered)

# filtering rows salary >55000 or age>30
filtered=df[(df['Age']>30)|(df['Salary']>55000)]
print("Employees with Salary greater than 55000 or Age greater than 30:")
print(filtered)