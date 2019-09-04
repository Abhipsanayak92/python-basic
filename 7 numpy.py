# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:06:10 2019

@author: user
"""

#%% 
import numpy as np
np.__version__ ###double underscore

#%% 1 D array
a=np.array([1,2,3])
print(a)
print(type(a)) #ndarray means N dimentional array
print(a.ndim) #to find out which dimension array

#%% 2D array
a=np.array([(1,2,3), (4,5,6)])
print(a)
print(a.ndim)
print(a.shape) #to find no of rows and columns

a=np.array([(1,2,3), (4,5)])
print(a) #converted to 1D, as both array not equal in size
print(a.ndim)
print(a.shape) #to find no of rows and columns

#%% 
a=np.array([(1,2,3,4),(4,5,6)])
print(a)
print(a.ndim)
print(a.shape) #in 1D array, it will return only no of elements

#%% ones() will replace each element of array with 1
a,b = np.ones((2,3,4)) #it means ones(howmany array need to be created, no of rows, no of columns)
print(a)
print() #to print empty line
print(b)

a,b =np.ones((2,3,4), dtype=np.int) #we are converting datatype as integer
print(a)
print() #to print empty line
print(b)
#%% zeros(0 used to replace with each element in array)
a,b =np.zeros((2,3,4)) #by deafult datatype is float
#it means zeros(howmany array need to be created, no of rows, no of columns)
print(a)
print() #to print empty line
print(b)

a,b =np.zeros((2,3,4), dtype=np.int) #we are converting datatype as integer
print(a)
print() #to print empty line
print(b)

#%% to create array of userdefined value

c,d=np.full((2,2,2),5.6) #it means full(howmany array need to be created, no of rows, no of columns)
print(c)
print(d)


#%% to create identity matrix (diagonal elements are 1)
a=np.identity(3, dtype=np.int)
print(a)


#%%
a= np.random.random((5,2)) #we need 5cross 2 matrix
#random function is inside random package
#random package is inside numpy package
print(a)

a=np.random.random_integers(50,100,(3,4))
#need random no between 50 to 100 and 3 cross 4 matrix
print(a)

#%% 
a=np.array([(1,2,3,4),(4,5,6,7)])
print(a)
print(a.size) #size tells total no of elements in array
print(a.shape) #no of rows and columns

#%% resize() used to modify array
#reshape is to change shape of array

a=np.resize(a,(6,3)) #repeats elememts to resize as original size 2cross4, now 6 cross 3

print(a)

a=np.resize(a,(2,3)) #removes elements to resize as original size as 2 cross 4 and now 2 cross 3
#a=np.reshape(a,(2,9)) #it will get total no of elements as original array, only shape will be changed
#(6,3)= (2,9)=(1,18) etc
print(a)

#%% indexing and slicing
a=np.array([(1,2,3,4), (3,4,5,6), (8,9,10,11)])

print(a)
print(a[0,2]) #access elements of (row number, column number)
print(a[:,2]) # :means all, it will access all row and 2nd column only
print()
print(a[0:2, :]) # it will include 0th row, 1st row, it will not include 2nd row, all columns

#%% linspace() used 
a= np.linspace(1,5,5)
a= np.linspace(1,10,5)  #1st 2 elements are range, 3rd element is how many parts u want to divide the array 
print(a)

a= np.linspace(100,10,5)
print(a)

a=np.arange(0,25,5) #2nd argument is exclusive
# here 3rd arguments will be act as incremental value
print(a)

a=np.arange(100,19,-2) ##as decreasing order 
print(a)

#%% aggregate functions
a=np.array([(8,9),(10,11),(12,13)])
print(len(a))
print(a.min())
print(a.max())
print(a.sum())
print(a.sum()/a.size)
print(a.mean())

#%% math functions
import numpy as np
a=np.array([(1,0,3),(3,4,5)])

print(np.sqrt(a))
print(np.std(a))
print(np.log(a)) #log(0) =-infinity

b=np.sqrt(a)
print(b.round(2)) ##rounded off to 2 decimal point

#%%
x=np.array([(1,2), (3,4)])
y=np.array([(5,6), (3,4)])
print(x)
print(y)
print(x+y)
print(np.add(x,y))

print(x-y) #np.subtract()
print(x*y) #np.multiply() ##array multiplication
print(x/y) #np.divide()
print(x%y) #np.remainder()
print(x@y) #np.dot() #proper matrix multiplication

#%% help
?np.mean
print(np.lookfor("mean))
help(np.zeros)

#%%joining arrays
print(x)
print(y)
d=np.concatenate((x,y), axis=0) ##equivalent to vstack())
#axis decides which type of concatenation u want to perform
#axis=0 means row level
#axis =1 means column level
#bydefault axis = 0
print(d)


#conctaenate() , hstack, vstack can be used only if both arrays are having same dimension)
d=np.concatenate((x,y), axis=1) #equivalent to hstack()
print(d)

print()
print(np.vstack((x,y))) 
print(np.hstack((x,y)))

#%% ravel() used to converting array into single row 
print(x)
z=x.ravel() #converts 2D to 1D
print(z)
print(z.reshape(2,2))

#%% append() used when both arrays dimension is different
x=np.array([(1,2,3),(3,4,5)])
y=np.array([(6,7),(9,10)])
new_array=np.append(x,y)

print(new_array)

new_array=np.reshape(new_array, (5,2))
print(new_array)

#%% 
#insert() used to insert element in between arrays
x=np.array([(1,2,3), (4,5,6)])
new_array=np.insert(x,[1,3], 10) #here 1 and 3 will be replaced by 10
print(new_array)

new_array= np.insert(x, [1,3], [7,10])  #2nd argument is which index u want to add
#3rd argument is what values u want to write in those indexes
print(new_array)

#%%delete data from array

new_array=np.delete(newarray, [1,2])
print(new_array)

#%%
#replacing elements
new_array[4] =11 #4th index element will be replaced by 11
print(new_array)

#%%IMPORTING ###################################################doubt
my_array3=np.genfromtxt(r'D:\DATA SCIENCE DOCS\Python docs\7 array importing.txt', 
                        skip_header=1, delimiter=",", filling_values=0, unpack=False,
                        dtype= np.int)

print(my_array3)

my_array3=np.genfromtxt(r'D:\DATA SCIENCE DOCS\Python docs\7 array importing.txt', 
                        skip_header=1, delimiter=",", filling_values=0, unpack=True,
                        dtype= np.int)

print(my_array3)   #unpack = true will transpose the array
#write r before path else it will show error