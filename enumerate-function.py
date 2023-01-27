# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:59:36 2023

@author: PC
"""
#%%
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print()

for count, item in enumerate(grocery):
  print(count, item)

print()

# changing default start value
for count, item in enumerate(grocery, 100):#start index:100
  print(count, item)
