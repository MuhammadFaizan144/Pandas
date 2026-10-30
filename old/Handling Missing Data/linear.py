import pandas as pd
data = {
    "Time": [1, 2, 3, 4],
    "Value": [10, None, None, 40]
}
df = pd.DataFrame(data)
print("before interpolation:")
print(df)


df['Value'] = df['Value'].interpolate(method='linear')
print(df)