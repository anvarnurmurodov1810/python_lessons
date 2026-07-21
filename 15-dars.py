# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:46:11 2026

@author: User
"""

python_izohli_lugati={'string':'matn',
                      'float':"o'nli kasr",
                      'integer':'butun son',
                      'dictionary':"lug'at",
                      'tuple':'uzgarmas jadval',
                      'if':'agar',
                      'else':'aks holda',
                      'for':'uchun'
                      }

#for key,valeu in sorted(python_izohli_lugati.items()):
     #print(f"{key.title()} - {valeu}")
     
     
davlat_poytaxt={'Uzbekistan':'Toshkent',
                'Spain':'Madrid',
                'France':'Parij',
                'England':'London',
                'Mexico':'Mexico',
                'Brazil':'Brazil',
                'Usa':'Washington'
                }
#print("ba'zi davlatlar va ularnig poytaxtlari")
#for davlat in sorted(davlat_poytaxt):
    #print(davlat)
#print("")    
#print("Davlatlarning poytaxlari")
#for poytaxlar in sorted(davlat_poytaxt.values()):
 #print(poytaxlar)                
     
#country=input("qaysi davlatning poytaxtini bilishni xohlaysiz ? :").title()
#capital=davlat_poytaxt.get(country)
#if capital==None:
    #print("bunday davlat jadvalda yuq")
#else:
    #print(f"{country.title()} ning poytaxti {capital.title()}")

menu={'osh':'15000',
      "lag'mon":'20000',
      'manti':'25000',
      'somsa':'15000',
      'shashlik':'30000'
      }
print("3 ta taom buyurtma bering:")
buyurtmalar=[]

for n in range(3):
    buyurtmalar.append(input(f"{n+1} taomni kiriting:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"kechirasiz bizda {buyurtma} yuq")
        








