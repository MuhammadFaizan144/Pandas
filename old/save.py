import pandas as pd
data={
    "Name":["Faizan","Ali","Ahmed"],
    "Age":[12,67,45],
    "City":["Lahore","Karachi","Islamabad"]
}
df=pd.DataFrame(data)
print(df)
df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)
df.to_json("output.json",index=False)