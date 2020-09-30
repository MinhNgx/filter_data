import pandas as pd

df = pd.read_excel(r"C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\python_filter.xlsx")

#print('Len:',len(df))
#df.info()
#print('Shape',df.shape)
print(df)

#split_df = df['Address'].str.split(",")
#data = split_df.tolist()
#new_df = pd.DataFrame(data)
#print(split_df)