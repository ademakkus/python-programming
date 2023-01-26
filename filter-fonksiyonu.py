# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 09:25:48 2023
#%% : run current cell alanı oluşturmak için kullanılır.katlanabilir kod alanı oluşturur.
spyder ide deki ,ikinci sıradaki çalıştırma butonu
@author: PC
"""
#%%
sayilar=[3,2,5,-7,12,4,-5,-6,-3,11,100,-2,22,33]
def pozitifMi(s):
    return s>0
for sayi in sayilar:
    if sayi>0:
        print(sayi)
print(pozitifMi(4))
print(pozitifMi(-4))
print(pozitifMi(0))
#pozitif sayılar
pozitifSayilar1=filter(pozitifMi,sayilar)
print(pozitifSayilar1) #pozitifSayilar1, filter object türündendir. bunun listeye dönüştürülmesi gerekir
pozitifSayilarListe=list(filter(pozitifMi,sayilar))
print('+++ Pozitif Sayılar Listesi ++++')
print(pozitifSayilarListe)
print('+++lambda Kullanılarak Pozitif Sayılar Listesi ++++')
pozitifSayilarListe2=list(filter(lambda s:s>0,sayilar))
print(pozitifSayilarListe2)
print('+++generate yaparak Pozitif Sayılar Listesi ++++')
pozitifSayilarListe3=[sayi for sayi in sayilar if sayi in pozitifSayilar1]
print(pozitifSayilarListe3)

#negatif sayılar
print('-- lambda Kullanılarak Negatif Sayılar Listesi ----')
negatifSayilarListe=list(filter(lambda s:s<0,sayilar))
print(negatifSayilarListe)
print('---- generate yaparak Negatif Sayılar Listesi ----')
negatifSayilarListe2=[sayi for sayi in sayilar if sayi not in pozi]
print(negatifSayilarListe2)
