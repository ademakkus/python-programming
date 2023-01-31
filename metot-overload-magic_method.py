# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:04:26 2023

@author: PC
"""
#%%magic method ile metot overload
class Nokta:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        '''
        artı + operatörü aşırı yükleme metodu
        :param other: Nokta türünde parametre
        :type other: Nokta
        :return: iki noktayı toplayıp yeni bir nokta olarak döndürür
        :rtype: Nokta

        '''
        x=self.x+other.x
        y=self.y+other.y
        return Nokta(x,y)
    def __str__(self):
        '''
        to string metodu overload ediliyor
        :return: str türünde
        :rtype: str

        '''
        return f'({self.x},{self.y})'
nokta1=Nokta(12, 13)
nokta2=Nokta(-4, -6)
yeninokta=nokta1+nokta2
print('Nokta1:{0}, Nokta2:{1}ve yeni nokta {2}'.format(nokta1,nokta2,str(yeninokta)))

