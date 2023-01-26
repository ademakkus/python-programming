# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:52:39 2023

@author: PC
The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working :  

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
"""
#%%
from functools import reduce
sayilar=[1,2,3,4,5,6,7,8,9,10]
def topla(s1,s2):
    return s1+s2
toplam=reduce(topla, sayilar)
print(toplam)
fark=reduce(lambda s1,s2:s1-s2, sayilar)
print(fark)
# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
import functools

# importing operator for operator functions
import operator

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))


def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)