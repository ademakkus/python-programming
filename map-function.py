# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:03:29 2023
#%% : run current cell alanı oluşturmak için kullanılır.katlanabilir kod alanı oluşturur.
spyder ide deki ,ikinci sıradaki çalıştırma butonu
@author: PC
We can use the Python built-in function map() 
to apply a function to each item in an iterable 
(like a list or dictionary) and return a new iterator for retrieving the results.
 map() returns a map object (an iterator), which we can use in other parts of our program. 
 We can also pass the map object to the list() function, or another sequence type, 
 to create an iterable.
 map(fun, iter)
 Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
"""
#%%
sayilar=[3,2,5,-7,12,4,-5,-6,-3,11,100,-2,22,33,110,55]
def kareAl(s):
    return s**2

sayilarKaresi=[]
for sayi in sayilar:
    sayilarKaresi.append(sayi**2)
print(sayilarKaresi)
#generate kullanarak
print('generate kullanarak')
sayilarKaresi2=[sayi*sayi for sayi in sayilar]
print(sayilarKaresi2)
#map kullanarak
print('map kullanarak')
sayilarKaresiMap=map(kareAl,sayilar) #map türünde döndürür
sayilarKaresi3=list(sayilarKaresiMap)
print(sayilarKaresi3)
#lambda kullanarak
print('lambda ve map kullanarak')

sayilarKaresi4=list(map(lambda s:s*s,sayilar))
print(sayilarKaresi4)
# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
print('Add two lists using map and lambda')
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
# List of strings
liststr = ['sat', 'bat', 'cat', 'mat']
print('# List of strings')
# map() can listify the list of strings individually
test = list(map(list, liststr))
print(test)
#[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]


