# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:34:13 2019

@author: Narendra
"""
#%%
''' Data structure
1. Numbers  (int, float, complex)
2. String   (immutable)
3. List (mixed data type, repeatative element, preserves the order, mutable, [])
4. Tuples (mixed data type, repeatative element, preserves the order, immutable, ())
5. Sets
6. Dictionaries '''

#%%
# 1. Numbers
a= 4
print(type(a))

b= 30.6
print(type(b))

c= 10+ 2j
print(type(c))

#%%
print(int(-2.8))

print(float(5))
        
#%%
## import math library and execute function

import math  ##import library

print(math.sqrt(4))
print(math.floor(-10.7))
print(math.pow(2,3))
print(math.pi)
print(math.factorial(6))

#%%
## import random library and execute
import random as rn

print(rn.random())   ## random number range b/w 0 to 1
print(rn.randrange(50,100)) ## for integers
print(rn.uniform(50.5,100)) ## for float

#%%
x= ['a', 'b', 'c', 'd', 'e']  
print(rn.choice(x))
print(rn.choices(x, k=3))  ####any 3 numbers will be picked randomly

#%%
rn.shuffle(x)
print(x)

#%%
# 2. String

my_string = "Hello World"
print(my_string)

#%%

my_string1 = """ I am Narendra
                 I am learning Python
                 Nikita is my trainer"""
print(my_string1)

#%%

my_string2 = "Hi everyone\n This is Jay"
print(my_string2)

#%%
#Slicing
my_string = "Python is a programming language. Python is interesting."
print(my_string[0])
print(my_string[-3]) #from ending,3rd letter, includes .
#[inclusive:exclusive]
print(my_string[3:10]) #includes 1st index, excludes last index
print(my_string[:25])
print(my_string[25:])
print(my_string[:])
print(my_string[100]) #as 100th index not there

#%%
#Delete function
del my_string

#%%
print(my_string) 
## NameError name my_string is not defined

#%%

str1 = "Hello"
str2 = "World!"
str1=str1+" "+str2
print(str1)

#%%

print("PyThOn".lower())

data = "python, is, a, programming language."
print(data.upper().split(sep= ","))

print("Happy Diwali".replace('p','d'))

#%% 
# LISTS
mylist1 = [1,3,4,2,5]
mylist2 = [1,4.2,'Python', 4.2]

print(mylist1)
print(mylist2)
print(type(mylist2))

#%%
print(list(range(0,10)))

#%%
#lists are mutable (replace value without replace with index number)

a= [10,20,30,40,50,60,70,80,90]
print(a)
a[3] = 55.0
print(a)

#%%
# nested list
b = ['spam', 2.0,5,[10, "raj"]]
print(b[2])
print(b[3])
print(b[3][1])

#%%
# + character for concatenate
c=  a+b+[5,6]
c

#%%
# appending a single element
# (append used for adding single element at a time)

my_list =[1,2]
i=1

while(i<5):
    value = input("Enter an element : ")
    my_list.append(value)
    i+=1
print(my_list)    

#%%

# appending multiple element at a time
my_list = [1,3,5.2,7]
my_new_list = [2,4,6,'Jay']

my_list.extend(my_new_list)

print(my_list)

type(my_list)

#%%
list1 = ['a', 'd','b','c','d','e','f']  
list1.insert(1,"p")
print(list1)
print(list1.index("p"))

#%%
list1.reverse()
print(list1)

#%%
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#%%
b= ['spam',2,3.5,[10,"jay"]] 
b.sort()

#%%

del list1[4]
print(list1)

list1.remove('d')
print(list1)

del list1[1:3]
print(list1)

#%%
#  copy function
list2 = list1.copy()   
list2

#%%

list1.clear() 
#%%

#aggregate function
num = [5,10,15,20,25,30]
#num = ["p",2.5, 'python']

print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))

#%%
# Lists and strings
x=(1,2,3,4,5)
#x="Jay Ram"
y=list(x)
print(y)
type(y)

#%%
# Zip function
a= [10,20,30,40,50,60]
b= [2,4,6,8,10]
print(list(zip(a,b)))

#%%
## 3. TUPLES

a= (5,'python',10+2j)
print(type(a))
print(a[0])

#%%
# Empty Tuple
c=()
print(type(c))

c=tuple("python")
print(c)

#%%
n_tuple = ("mouse", [8,4,6],(1,2,3),8)
print(n_tuple[1])

print(n_tuple[1][2])

print(n_tuple)
print(n_tuple[2][1])

del n_tuple[1][2]
print(n_tuple)

del n_tuple

