# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:17:04 2023

@author: PC
"""
#%%
class Genel:
    def __init__(self,baslik,icerik,gorsel):
        self.baslik=baslik
        self.icerik=icerik
        self.gorsel=gorsel
    def bilgileriGoster(self):
        print(self.baslik,self.icerik,self.gorsel)
    
class Spor(Genel):
    def __init__(self, baslik, icerik, gorsel,video):
        super().__init__(baslik, icerik, gorsel)#ata sınıf (Genel) constructor metodu çağrılıyor
        self.video=video
    def bilgileriGoster(self):
        super().bilgileriGoster()#ata sınıf (Genel) bilgileriGoster() metodu çağrılıyor
        print(self.video)
    def videoOynat(self):
        print(self.video+' videosu oynatılıyor...')

class Finans(Genel):
    def __init__(self, baslik, icerik, gorsel,dovizKurlari):
        super().__init__(baslik, icerik, gorsel)
        self.dovizKurlari=dovizKurlari
    def dovizKuruGoster(self):
        super().bilgileriGoster()
        print('--Döviz Kurları---')
        for dovizAdi,dovizDegeri in self.dovizKurlari.items():
            print(dovizAdi,":",dovizDegeri)
            
sporHaber1=Spor(baslik='Berabere Biten Derbi', icerik='Çok çekişmeli maç berabere bitti.', gorsel='resim.jpg', video='video1.mp4')
sporHaber1.bilgileriGoster()
finansHaber1=Finans(baslik='Günlük Döviz Kurları', icerik='Doviz fiyatları artış sürecine girdi', gorsel='doviz.jpg', dovizKurlari={'Dolar':18.0,'Euro':20.0,'Sterlin':22.0})
#finansHaber1.bilgileriGoster()
finansHaber1.dovizKuruGoster()
                                                                                                                                    