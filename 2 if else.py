# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 10:37:25 2019

@author: Narendra
"""
#%%
# if else
x= 3
y= 5

if x < y:
    print("This is the first block")
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
print("Done")

#%%
# nested if else
if x==y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
print("Done")

#%%

choice1 = int(input("Enter 1/2/3: "))
  
print(choice1)

if choice1 == 1:
    print('Bad')
elif choice1 == 2:
    print('Good')
elif choice1 == 3:
    print('Close')
else:
    print('Enter the correct number')
    
#%%
choice1 = float(input("Enter 1/2/3: "))
choice1 = round(choice1,0) #rounded off to 0th decimal
if choice1 == 1:
    print('Bad')
elif choice1 == 2:
    print('Good')
elif choice1 == 3:
    print('Close')
else:
    print('Enter the correct number')
    
#%%
choice1 = float(input("Enter 1/2/3: "))
choice1 = round(choice1,0) #rounded off to 0th decimal
if choice1 == 1:
    print('Bad')
elif choice1 == 2:
    print('Good')
elif choice1 == 3:
    print('Close')
#%%
x=5
y=8
if (x>7 and y>7) or x!=y:
    print("x is a positive single digit number")
