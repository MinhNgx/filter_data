# load pandas
import pandas as pd
raw_data = pd.read_csv(r"C:\Users\vanminh1\OneDrive - Intel Corporation\Desktop\gapminder-FiveYearData.csv")

# show data
print("Raw_data")
print(raw_data.head(3))

# does year equals to 2002?
# is_2002 is a boolean variable with True or False in it
is_2002 = raw_data['year']==2002
print(is_2002.head())

# filter rows for year 2002 using the boolean variable
data_2002 = raw_data[is_2002]
print("Data_2002 = ",data_2002.shape)
print("Data_2002")
print(data_2002.head())

# filter rows for year does not equal to 2002
data_not_2002 = raw_data[raw_data['year']!=2002]
print("Data_not_2002")
print(data_not_2002.shape)

#To select rows whose column value is in list 
years = [1952, 2007]
data_years= raw_data[raw_data.year.isin(years)]
print("Data_1952-2007 = ",data_years.shape)

#To select Rows of Pandas Dataframe Based on Values NOT in a list
continents = ['Asia','Africa', 'Americas', 'Europe']
data_Ocean = raw_data[~raw_data.continent.isin(continents)]
print("Data_ocean = ",data_Ocean.shape) 

#To select Rows of Pandas Dataframe using Multiple Conditions
data_multiple = raw_data[~raw_data.continent.isin(continents) & raw_data.year.isin(years)]
print("Data_Multiple")
print(data_multiple.head())