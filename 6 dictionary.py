# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:29:37 2019

@author: user
"""

#Dictionaries:
#{key:value, k:v}
#it has unique keys only
#in dictionary repeatitive values are allowed
#values are mutable
#mixed data types are allowed
#accessing done using keys, not ny indexes

#%% creation of dictionary
my_d= {}

my_d= {1: 'A', 2: "B"}
print(my_d)

my_d= {'name': "John", "ID": [2,4,3]}
print(my_d)

my_d= dict([("fruit", "apple"), (2, "ball"), ("fruit", "mango")])  #it will take exactly 2 values as one will b considered as key and another as value
print(my_d) #here mango will replace apple as repetitive keys not allowed
#dict is used to type cast dictionary

my_d= dict([("fruit", "apple"), (2, "ball"), ("vegetable", "mango")])  #it will take exactly 2 values as one will b considered as key and another as value
print(my_d)

my_d= dict([("fruit", "apple"), (2, "ball"), ("mango", "fruit")])  #it will take exactly 2 values as one will b considered as key and another as value
print(my_d)

my_d= dict([("fruit", "apple"), (2, "ball"), ("mango", "fruit", "banana")])  #gives error as it will take exactly 2 values as one will b considered as key and another as value
print(my_d)


#%% accessing values
my_d= {"name":"ABHIPSA", "age": 25}
print(my_d["name"])

print(my_d["add"]) ##gives error as add is not as key in dictionary


#never keep file name as any object name like dictionary or numpy


#%% updating
my_d["age"]=12
print(my_d)

my_d["age"]=13
print(my_d)#replace 12 by 13 as keys are unique

my_d["address"] ="Mumbai"
print(my_d)

#%%deleting
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

del squares[5] #it will delete key of 5, so this 5 is key , not index
print(squares)

del squares  #will delete entire object

#squares.clear#it will empty the dictionary
#print(squares)

#%% how to find what are keys and what are values present in dictionary

squares.values() #to find what are the values present in dictionary

squares.keys() #to find what are the keys are present in dictionary
