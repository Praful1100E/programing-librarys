import pandas as pd

# Creating a series
# data = pd.Series([1, 2, 3, 4, 5])
# print(data)

# Creating a DataFrame
# data={"Name": ["John", "ram", "sita", "tushar", "Delta"]}
# df=pd.DataFrame(data)
# print(df)

# To reade a CSV file
# df = pd.read_csv('data.csv')
# print(df)

# Write csv file
# df.to_csv("Output.csv",index=False)


# Exploring Data
# df.hed() First 5 rows
# df.tail() Last 5 rows
# df.shape() row and column
# df.columns() column 
# df.info() Information about DataFrame
# df.describe() Summary statistics of DataFrame
# df.dtypes() Data types of each column
# df.isnull() Check for null values
# df.notnull() Check for non-null values
# df.isnull().sum() Count of null values in each column
# df.notnull().sum() Count of non-null values in each column