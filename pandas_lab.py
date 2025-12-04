# importing pandas
import pandas as pd
# creating data frame
dictionary = {"Name":['Alice','Adam','Bob','Charlie',None],"Age":[25,24,None,35,30],"City":['New York',None, 'Los Angeles',None,'Chicago'],"Team":['A','B','B','C',None]}
data = pd.DataFrame(dictionary)
#saving the data frame in csv
data.to_csv('data.csv')
# viewing the first few rows
print(data.head(2))
# display dataset shape and column names
print(data.columns)
# checking for missing values using ISNULL() function
print(pd.isnull(data))
#checking for missing values using NOTNULL() function
print(pd.notnull(data))
# fill all missing values with 0 using fillna
print(data.fillna(0))
# fill missing values in column "Names" with "Username"
data['Name'].fillna("Username", inplace=True)
# fill missing data with forward
data['Team'].fillna(method='ffill', inplace=True)
# fill all missing values with the backward filling
data['City'].fillna(method='bfill', inplace=True)
# fill all missing value with the mean of numerical column
mean_value = data['Age'].mean()
data['Age'].fillna(mean_value, inplace=True)
# drop rows with missing values using DROPNA()
new_data=data.dropna()
# save your updated dataframe into new CSV
new_data.to_csv('new_data.csv')

