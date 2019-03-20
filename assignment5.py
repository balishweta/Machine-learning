#a.) Find the sum of missing data for every column in the dataset using the (isnull function and sum function)

import pandas as pd
new_df = pd.read_csv("weather.csv",delimiter=',')
print(new_df.isnull().sum())
#print(new_df.describe())
#print(new_df.head(20))

#b.) Remove the missing values (if any)
#Pandas provides the dropna() function that can be used to drop either columns or rows with missing data.
#We can use dropna() to remove all rows with missing data, as follows:

new_df.dropna(inplace=True)
print(new_df.isnull().sum())


#c.) Once again , Import the dataset and this time replace the missing null values with mean of the column series.

new_df.fillna(new_df.mean(), inplace=True)
print(new_df.describe())

#d.) Find individual data types and copy the temperature column to a pandas series.

print(new_df.dtypes)

s=pd.Series(new_df["Temp9am"])
print(s)


