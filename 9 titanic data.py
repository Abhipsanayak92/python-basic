# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 16:17:09 2019

@author: user
"""


#%%
pd.set_option('display.max_columns',None)

pd.set_option('display.max_rows', None)

#%% titanic data

import pandas as pd

titanic_df=pd.read_excel(r"D:\DATA SCIENCE DOCS\Python docs\9 Titanic_Survival_Train.xls",index_col=0,header=0)

titanic_df

titanic_df.head() #default value 5, it will show top 5 observation 

titanic_df.head(7) #default value 5, it will show top 7 observation 

titanic_df.tail() #default value 5, it will bottom 5 observation 

titanic_df.dtypes

titanic_df.info()

titanic_df.shape

#%% describe() gives descriptive statistics in  numerical variables

titanic_df.describe() #it will show whioch values are not having any missing values
#we can chq missing value from this also

titanic_df.describe(include="all") #for both numerical and categorical variable

titanic_df.Sex.describe()

#%%subsetting
my_df=titanic_df[["Sex", "Pclass", "Age"]]
print(type(my_df)) #dataframe
print(my_df)

my_df=titanic_df["Sex"]
print(type(my_df)) #series

#%%filtering
df_agemorethan60=titanic_df[titanic_df["Age"]>60]
df_agemorethan60
df_agemorethan60.shape

#%%multiple filtering
my_df=titanic_df[(titanic_df["Age"]>60) & (titanic_df["Sex"]=="male") & (titanic_df["Survived"]==1)]
my_df.shape[0] #shape of only row
my_df.shape

#%% tabulation
print(titanic_df.Embarked.value_counts()) 
#value counts() is for categorical variable, for numerical value output is not so much interpretable
#value counts works on single variable 
#it will give unique values in a variable


#%% crosstab() works to see 2 variable contingency table  (not more than 2)
pd.crosstab(titanic_df["Sex"], titanic_df["Survived"])


#%%sex wise survival rate
print(titanic_df["Sex"][titanic_df["Embarked"]=="S"] [titanic_df["Survived"]==1].value_counts())

print(titanic_df["Sex"][titanic_df["Embarked"]=="S"] [titanic_df["Survived"]==0].value_counts())

#%% discretization and binning

PassengerAge=titanic_df["Age"]
PassengerAge = PassengerAge.dropna() #dropna() will drop all missing value in variable
Bins=[0,15,21,60,PassengerAge.max()]
Binlabels=["Children", "Adolescents", "Adult", "Senior"]
categories=pd.cut(PassengerAge, Bins, labels=Binlabels, include_lowest=True) #bydefault lowest=True, if u want to ignore lowest, then write lowest =False
#cut() used to create the range and assign values in the range accordingly
#categories=pd.cut(PassengerAge, Bins, labels=Binlabels, include_lowest=False)
print(categories.value_counts())
print(categories)

#%%
new_df=pd.concat([PassengerAge,categories], axis=1) #column wise
new_df.head(10)
new_df.columns=["Age", "Category"]
new_df.head(10)

new_df=pd.concat([PassengerAge,categories], axis=0)  #row wise
new_df.head(10)

#%% treating missing values
print(titanic_df.isnull())  #gives boolean value
print(titanic_df.isnull().sum())#gives total no of missing values in each variable
print(titanic_df.isnull().any(axis=1).sum()) 
#total no of missing values present in total dataset both row wise and columnwise.
#means out of total observations, how many observations are having missing values(may be 1 column or may be more than one missing values)
# means if in any row, one or more than one missing value will be present then it will consider it one
#it will help us to give an idea whether to eliminate rows or treat missing values
#output is 708 means out of 891 obs, 708 obs are having missing values
print(titanic_df["Age"].isnull().sum()) #to find variable wise missing values


#%%
#print(titanic_df.dropna()) #drops all obs containing missing value and output will be without missing values
new_df=titanic_df.dropna() #creating another dataframe without missing values
new_df.shape
#%%
#print(titanic_df.fillna(0)) #fill with value 0 in all missing values
new_df=titanic_df.fillna(0)
#fillna() should never be done on total dataframe as every missing values in each variable can be different
new_df.shape


#%%
half_count=len(titanic_df)/2

titanic_df=titanic_df.dropna(thresh=half_count,axis=1)
print(titanic_df.isnull().sum())
#i have created condition as threshold that if my total obs in a variable contains missing values, then drop that variable
#here cabin has been dropped bcz it has more than 50%(threshold) missing values
"""
half_count=0.75*len(titanic_df)
print(half_count)
"""


#%% handling missing values in Ticket column
titanic_df=titanic_df.drop("Ticket", axis=1)
titanic_df.head()

#%% handling missing values in embarked column
titanic_df["Embarked"].fillna(titanic_df["Embarked"].mode()[0],inplace=True)
print(titanic_df.isnull().sum())
#inplace=true means wherever will be missing values, S will be replaced as mode = S
#here we have taken mode as embarked is categorical,
#we can use mean instead for numerical values
#titanic_df["Embarked"]=titanic_df["Embarked"].fillna(titanic_df["Embarked"].mode()[0],inplace=True)
#it is time consuming than inplace=True
#%%
titanic_df["Embarked"].mode() #mode is mostly used as treatemnt for categorical variable

#%% handling missing values in age column
titanic_df.Age.mean() #mean is for numeric variable
titanic_df["Age"].mean() #printing mean value
titanic_df["Age"].fillna(titanic_df["Age"].mean(),inplace=True)
print(titanic_df.isnull().sum())

titanic_df["Age"].fillna(round(titanic_df["Age"].mean(),0),inplace=True) 
#rounding off to 0 decimals for mean
print(titanic_df.isnull().sum())

#%% homework
pd.merge()
##create two df
"""
a- studentid, name, gender -df1
b- student id, marks, percentage - df2

make excel or csv
merge both a and b
"""

#difference between merge and concat