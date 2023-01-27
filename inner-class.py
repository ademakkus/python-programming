# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:44:26 2023

@author: PC
"""
#%%
class Musteri:
   def __init__(self,musteriNo,isim,soyad,bakiye,hesapTuru):
       self.musteriNo=musteriNo
       self.isim=isim
       self.soyad=soyad
       #self.bakiye=bakiye          #Hesap sınıfından alacak
      # self.hesapTuru=hesapTuru    #Hesap sınıfından alacak
       self.hesap=self.Hesap(bakiye,hesapTuru)
    
   def bilgileriGoster(self):
      print(f'Müşteri No:{self.musteriNo},Müşteri İsmi:{self.isim}, Müşteri Soyadı : {self.soyad}')
      self.hesap.bilgileriGoster()
     
   class Hesap:
     def __init__(self,bakiye,hesapTuru):
            self.bakiye=bakiye
            self.hesapTuru=hesapTuru
     def bilgileriGoster(self):
        print(f'Bakiye: {self.bakiye} Hesap Türü: {self.hesapTuru}')
       
       
musteri1=Musteri(1,'Adem','AKKUŞ',100000,'TL')
musteri1.bilgileriGoster()      
 
musteri2=Musteri(2,'Gülten','ALDEMİR',10000,'DOLAR')
musteri2.bilgileriGoster()

musteri3=Musteri(3,'Furkan','AKKUŞ',20000,'EURO')   
musteri3.bilgileriGoster()  
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
   
   
       
     
    
    