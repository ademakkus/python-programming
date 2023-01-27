# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 23:44:20 2023

@author: PC
"""
#%%
class Insan:
    def __init__(self):#default constructor
        pass
    def __init__(self,ad,soyad,yas,meslek):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.meslek=meslek
    def bilgileriYazdir(self):
        print(f'Adınız:{self.ad}\nSoyadınız:{self.soyad},\nYaşınız:{self.yas}ve \nMesleğiniz:{self.meslek}')
#insan=Insan()
insan2=Insan('Adem', 'AKKUŞ', 40, 'Bilgisayar Mühendisi')
#insan.bilgileriYazdir()
insan2.bilgileriYazdir()

