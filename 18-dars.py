# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:26:44 2026

@author: User
"""


#savat=[]

#while True:
 #   buyurtma=input("mahsulot nomini kiritng : ")
#    savat.append(buyurtma)
   # savol=input("keyingi mahsulotning kiritasizmi ? (ha/yoq) : ")
  #  if savol !="ha":
 #       break

#print(savat)

mahsulotlar={}
#while True:
 #   mahsulot=input("mahsulot nomini kiriting: ")
 #   narh=input('{mahsulot}-ning narhini kiriting:')
 #   mahsulotlar[mahsulot]=narh
#    savol=input("yangi mahsulot kiritasizmi ? (ha/yoq) : ")
#    if savol!='ha':
#        break

mahsulotlar={'olma':'10 ming sum','anor':'15 ming sum','behi':'7 ming sum','qulupnay':'30 ming sum','qovun':'25 ming sum'}
buyurtmalar=['olma','tarvuz','ananas','behi','qulupnay']
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        print(f"{buyurtma} ning narhi-{mahsulotlar[buyurtma]}")
    else:
        print(f"kechirasiz bizda {buyurtma} mavjud emas")
        











