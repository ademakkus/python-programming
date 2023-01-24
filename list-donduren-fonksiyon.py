# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:27:12 2023

@author: PC
"""
from math import pi
def daireCevreVeAlan(r):
    return [2*pi*r,pi*r*r]
print(daireCevreVeAlan(10))
result=daireCevreVeAlan(6)
print(f'Dairenin Çevresi:{result[0]} ')
print(f'Dairenin Alanı:{result[1]} ')
cevre,alan=daireCevreVeAlan(8)
print(f"Daire Çevresi:{cevre} ")
print(f"Daire Alanı:{alan} ")
