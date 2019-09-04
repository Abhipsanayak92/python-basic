# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:26:17 2019

@author: user
"""

#set elements are unordered, means no ascending or descending order, order can be anytype
#it has unique elements, no repeat elements
#mixed datatypes can be present in a set
#mutable as a whole
#immutable for individual elements
#dosenot support indexing

#%%
my_set = {1,2,3,5,7,6,4,3,2,10,38,72,16}
print(my_set)

#%%
my_set= {1,1.0, "HELLO", "Manish", (1,2,4)}
print(my_set)

#%%
#my_set={1,2,[3,4]}  it will show error as list is not allowed inside a set
my_set= {1,2, (2,4)}  #tuples are allowed inside set
print(my_set)
my_set[1]

#%%
a={}
print(type(a))

#%%creating an empty set

a=set()
print(type(a))

#%% adding elements
my_set= {1,3}
print(my_set)

#my_set[0]=1   #gives error as indexing not possible as it is immutable for individual elements

my_set.add(8)  #add is to add individual element
print(my_set)

my_set.update([6,8], {1,4,5}, (15,12)) #update is to add multiple elements

my_set=my_set.update([6,8], {1,4,5}, (15,12), ((8,9), (15,12))) ###############################doubt
print(my_set)
my_set.update((10,12))

#%% removing elements
my_set={1,3,4,5,6}
print(my_set)

my_set.remove(6)
print(my_set)

#del my_set[2]  #gives error as not supporting indexing, it does not support multiple element removal in one go

print(my_set)

#aggregate functions as in lists

#%%union and intersection

A={1,2,3,4,5,9}
B= {4,5,6,7,8,10}

print(A|B)
print(A.union(B))

print(A&B)
print(A.intersection(B))

#%%difference
print(A-B)  #A-B means elements present in A but not in B
print(B-A)   #B-A means elements present in B but not in A

print(A.difference(B))  #same as A-B
print(B.difference(A))#same as B-A

#%%
