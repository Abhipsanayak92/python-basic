# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:13:37 2019

@author: user
"""

#%% importing pandas library
import pandas as pd

#%%
#for 1d data- series used(S capital)
#for 2d data - data frame is used (D and F captital)

"""4types of data type
1. int
2. float
3 object for categorical 
4 date -time"""

#%%  series
import numpy as np
data= np.array([101, 102,103,104])
s= pd.Series(data) #tabular form 1d data
print(s)
print()
print(s[1])
s[1]=100
print(s)

#%%
s= pd.Series(data, index=["a","b","c","d"])
print(s)
print(s["b"]) 
print(s[1]) #we can access from index type and also by name

s["b"]=30


#%%
list1=np.arange(1001,1005,1)
s=pd.Series(data, index=list1)
print(s)
print(s[1001])
print(s[1]) #will give error as previous index number will be overwritten by new index no

#%%
data= {"a":0., "b":1., "c":2.}
s=pd.Series(data)
print(s)
print[("a")] ##############giving error  
print()
print(s[-2:])

#%%
##DATA FRAMES
data= [["AMIT", 40], ["NIKITA", 50], ["CLARA",60]]
df=pd.DataFrame(data, columns=["Name", "Age"])   #naming indexes at the time of data creation
print(df)

data= [["AMIT", 40], ["NIKITA", 50], ["CLARA",60]]
df.columns=["Name", "Age"] #naming indexes after data creation
print(df)

#%% indexed data frame from dictionary
data={"Name":["Amit", "Nikita", "Clara"], "Age":[40,50,60]}
df=pd.DataFrame(data)
print(df)

df=pd.DataFrame(data, index= ["rank1", "rank2", "rank3"])
print(df)

df[["Name", "Age"]] ##accessing variables from total variables


#%% adding a column
df["Address"]=["Mumbai", "Pune", "Mumbai"] ##this format is for adding column in last
print(df)


df=df[["Name", "Address", "Age"]] #this format is to add column wherever u want to add
print(df)
df

#%%
df["Newcol"]=5
print(df)

df["Newcol"]= [5, 10, 15]
print(df)

df["Revisedcol"]= df["Newcol"]*2
print(df)

#%% deleting column

del df["Newcol"]
print(df)

#%% drop() used to remove both row and column
df=df.drop("rank1") #by deafult axis=0
print(df)
df.drop("Revisedcol", axis=1) #means column 
print(df)
df.drop("Revisedcol", axis=0) #gives error as revisedcol not available in rows , its in columns
print(df)


#%% accssing data elements using indexes and labels

# A) LOC location pass row label
# LOC[inclusive:inclusive]   -----> only to lables

# B) iloc passing index number
# iloc[inclusive:exclusive]  -----> only to index number

#df.loc[inclusive:inclusive]
print(df.loc["rank2"])
print(df.loc["rank2":"rank3"])
print(df)

print(df.iloc[0:1])#df.iloc[inclusive:exclusive]
#exclusive is only for index, not for row labels

print(df.loc["rank2":"rank3", ["Address", "Age"]])
print(df.iloc[:,[1,2]])

#%% viewing a subset
df[["Name","Age"]]


#%%
# Saving the current data set to the file to comeback and work on the 
# same dataset we use to_csv | to_excel
# saving df to a file

##for csv and txt files
df.to_csv(r'D:\DATA SCIENCE DOCS\Python docs\8 sampledf1.csv', index=True, header= True) #header is bydefault true


#for excel file
df.to_excel('8 sampledf2.xlsx') ##################################doubt
df.to_excel(r'D:\DATA SCIENCE DOCS\Python docs\8 sampledf2.xlsx',index= False, header= True)
print("Done")

#%% reading df from a file

df2=pd.read_csv(r'D:\DATA SCIENCE DOCS\Python docs\8 sampledf1.csv', index_col=0, header=0)
print(df2)

df2=pd.read_csv(r'D:\DATA SCIENCE DOCS\Python docs\8 april sampledf1.csv', index_col=1, header=0)
#1st column will be treated as indexing column
print(df2)

#%% ###################################3doubt
df3=pd.read_excel('8 sampledf2.xlsx')
print(df3)


df3=pd.read_excel('D:\DATA SCIENCE DOCS\Python docs\8 sampledf2.xlsx')
print(df3)

#%%preaparing data 
print(df.dtypes)  #data type of whole dataframe
print(df.Age.dtype) #data type of one variable
df.info() #overall information of whole data frame
print(df.shape)

#%% we have to set values within the set

df.set_value("rank2", ["Name", "Age"], ["Ramesh", 40])
df.set_value("rank4", ["Name", "Age"], ["Raj", 30]) #adding new column and set values
df.set_value(["rank2","rank3"], ["Name", "Age"], ["Ramesh", 40])

#%%
df
df.loc[(df.Name== "Ramesh") & (df.Address== "Pune"), ["Address", "Name"]]= ["Bangalore","Rahul"]
df


#%%
df.sort_values(["Address", "Name"], ascending= True) #for ascending order
##1st address will be sorted, then in mutual address, name will ne sorted
#by deafult ascending = True
df.sort_values(["Address", "Name"], ascending= False) #for descending order

#%%
print(df['Name'].unique())

#%% 
df.sort_index(axis=1, ascending = True)  #column level sorting
df.sort_index(axis=0, ascending = True)  #row level sorting

#%%