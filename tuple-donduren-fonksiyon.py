# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:15:02 2023

@author: PC
"""

def ucgenKenarGoster(kenar1,kenar2,kenar3):
    return f"Kenar-1:{kenar1}", f"Kenar-2:{kenar2}", f"Kenar-3:{kenar3}";#geriye tuple döndürür
print(ucgenKenarGoster(3, 4, 5))

print(type(ucgenKenarGoster(3, 4, 5)))
result=ucgenKenarGoster(3, 4, 5) #result tuple türünde

print(result[0])
print(result[1])
print(result[2])
kenar1,kenar2,kenar3=ucgenKenarGoster(3, 4, 5) #result tuple türünde
print(kenar1)
print(kenar2)
print(kenar3)