#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
import pandas as pd
d={"Name":['shweta'],"Age":[35],"Mail_id":['bali82.shweta@gmail.com'],"Phone_No":[9810328282]}
df = pd.DataFrame(data=d)
print('My data')
print(df)
print("appending the data of the friend")
df2={"Name":'Ritu',"Age":34,"Mail_id":'ritu1234@gmail.com',"Phone_No":9983728282}
print(df.append(df2,ignore_index=True))

#Q.2 - Download the dataset from this link ,Click Here
#Import the data and print the following :
#a.) First 5 rows of Dataframe
#b.) First 10 rows of the Dataframe
#c.) find basic statistics on the particular dataset.
#d.) Find the last 5 rows of the dataframe
#e.) Extract the 2nd column and find basic statistics on it.

#a) First 5 rows of Dataframe
import pandas as pd
new_df = pd.read_csv("data.csv",delimiter=',')
print('First 5 rows')

#b) First 10 rows of the Dataframe
print('first 10 rows')
new_df = pd.read_csv("data.csv",delimiter=',',nrows=10)
print(new_df)

#c)find basic statistics on the particular dataset.

print('find basic statistics on the particular dataset.')
print(new_df.describe())

#d.) Find the last 5 rows of the dataframe
print(new_df.head())
print('Last 5 rows')
print(new_df.tail())

#e.) Extract the 2nd column and find basic statistics on it.
print('Extract the 2nd column and find basic statistics on it.')
z=new_df['Location']
print('Extract the 2nd column')
print(z)
print('find the basics statistics on the extracted data')
print(z.describe())
