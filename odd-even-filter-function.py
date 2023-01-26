# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:03:29 2023
#%% : run current cell alanı oluşturmak için kullanılır.katlanabilir kod alanı oluşturur.
spyder ide deki ,ikinci sıradaki çalıştırma butonu
@author: PC
"""
#%%
sayilar=[3,2,5,-7,12,4,-5,-6,-3,11,100,-2,22,33,110,55]
ciftSayilar=list(filter(lambda s:s%2==0,sayilar))
print('++++ lambda Fonksiyonu Kullanarak Çift Sayılar +++++')
print(ciftSayilar)

#fonksiyon kullanarak çift sayıları bulma
def ciftMi(s):
    return s%2==0
ciftSayilar2=list(filter(ciftMi,sayilar))
print('++++ Fonksiyon Kullanarak Çift Sayılar +++++')
print(ciftSayilar2)
print('---lambda Fonksiyonu Kullanarak Tek Sayılar ---')
tekSayilar=list(filter(lambda s:s%2==1,sayilar))
print(tekSayilar)
#fonksiyon kullanarak tek sayıları bulma
def tekMi(s):
    return s%2==1
print('---Fonksiyon  Kullanarak Tek Sayılar ---')
tekSayilar2=list(filter(tekMi,sayilar))
print(tekSayilar2)