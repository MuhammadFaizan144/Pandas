import pandas as pd

data={
    "Name":["Faizan","Ali","Ahmed"],
    "Age":[12,67,45],
    "City":["Lahore","Karachi","Islamabad"]
}
df=pd.DataFrame(data)
# print(df)
print("Displaying the info of data set:")
print(df.info())