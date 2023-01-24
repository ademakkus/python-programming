# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:33:16 2022

@author: PC
"""

# while faktoriyel hesaplama
# 0!=1!=1
#a!=a.(a-1)...1
#4!=4.3.2.1
i=1
faktoriyel=1

sayi=int(input('faktoriyeli alınacak sayi giriniz:'))
while i<=sayi:
    faktoriyel=faktoriyel*i
    i+=1
    
print(sayi,'! =',faktoriyel)
    
    