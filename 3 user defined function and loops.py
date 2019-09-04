# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 13:04:08 2019

@author: Narendra
"""

    
#%%
# user defind function
def square(a):
    print("Value is =", a)
    return a*a 

value = float(input("Enter a number: "))
square(value)   

def s(a): #square is not an inbuilt function, we can give it any name 
    print("Value is =", a)
    return a*a

 
value = float(input("Enter a number: "))
s(value)

#%%
# while loop
count = 1
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached", count)    
    
#%%
friends = ['A','B','C',3.6]
for f in friends:    
    print("happy diwali", f)
    
    
#%%    
# for loop
friends = ['A','B','C',3.6,9]
for f in friends:
    if type(f)==str:
       print("It is a string value ", f)
    elif type(f)== int or float:
       print(f*f)
          
       
#%%       