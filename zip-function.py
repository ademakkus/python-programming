# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:38:08 2023
The zip() function returns an iterator of tuples based on the iterable objects.

If we do not pass any parameter, zip() returns an empty iterator
If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.
@author: PC
"""
#%%
numbers=[41,34,14,10,2]
names=['Adem','Gülten','Furkan','Ayşenur','Kerem']
cities=['Ankara','Corum','İstanbul','Kırşehir','İzmir']
zipped=zip(names,numbers)
print(zipped) #zip object
zippedlist=list(zipped)
zippedlist2=list(zip(numbers,names,cities))
print(zippedlist)
for element in zippedlist:
    print(element)
for info1,info2,info3 in zippedlist2:
    print(f'Number:{info1}, Name:{info2} and City:{info3}')