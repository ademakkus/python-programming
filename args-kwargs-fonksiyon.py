# -*- coding: utf-8 -*-
import math as mt
"""
Created on Wed Jan 25 17:31:56 2023
*ags: tuple türünde parametredir. adsız parametlerin yerine kullanılır.
   (1,2,3,4,5,6,7,8,9)
**kwargs: dictionary türünde parametredir. isimli parametredir
     islem='+' gibi
@author: PC
"""
def besIslem(s1,s2,*args,**kwargs):
    result=0
    #result=None
    stringResult=''    
    if kwargs['islem']=='+':
        result=s1+s2+sum(args)
        stringResult='Toplama İşlemi'
    elif kwargs['islem']=='-':        
        result=s1-s2-sum(args)
        stringResult='Çıkarma İşlemi'
    elif kwargs['islem']=='*':
        result=s1*s2*sum(args)
        stringResult='Çarpma İşlemi'
    elif kwargs['islem']=='/':        
         result=s1/s2/sum(args)
         stringResult='Bölme İşlemi'
    elif kwargs['islem']=='%':        
         result=s1-s2-sum(args)
         stringResult='Modalma İşlemi'
    else :        
         result=0
         stringResult='Geçersiz İşlemi'
    print(f'İşlem :{stringResult} ve sonuç={result}')
         

besIslem(12, 22, 1,2,3,4,5,6,7,8,9, islem='+')         
        
   