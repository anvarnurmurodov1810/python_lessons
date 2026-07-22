# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:55:09 2026

@author: User
"""

navoiy={'ism':'navoiy',
        'tyil':'1441',
        'manzil':'hirot',
        'asarlar':['xamsa','qush tili']}
xorazmiy={'ism':'muso-al xorazmiy',
          'tyil':'870',
          'manzil':'xorazm',
          'asarlar':['al-jabr val muqobala','hind raqamlari']}
ulugbek={'ism':'ulugbek',
         'tyil':'1397',
         'manzil':'samarqand',
         'asarlar':['yulduzlar haqida','1018 ta yulduz']}
bobolarimiz=[navoiy,xorazmiy,ulugbek]
#for shaxs in bobolarimiz:
    #print(f"\n{shaxs['ism'].upper()}"
          #f"\n{shaxs['tyil']}-yilda tug'ilgan"
          #f"\n{shaxs['manzil'].title()} da yashaydi"
         
#for shaxs in bobolarimiz:
    #ism=shaxs['ism']
    #asarlar=shaxs['asarlar']
    #print(f"\n{ism} ning mashxur asarlari")
    #for asar in asarlar:
        #print(asar.title())
kinolar={'davron':['departed','forest gump','chuqintirgan ota'],
         'abbos':['yulduzlar jangi 1','yulduzlar jangi 2','yulduzlar jangi 3']}
#for ism,kinolar in kinolar.items():                  
    #print(f"\n{ism.title()}ning sevimli kinolari:")
    #for kinolar in kinolar:
        #print(kinolar.title())
davlatlar={
           'uzbekistan':{'poytaxti':'toshkent',
                         'aholisi':'38 million',
                         'pul birligi':'sum'},
           'rossiya':{'poytaxti':'moskva',
                      'aholisi':'120 million',
                      'pul birligi':'rubl'},
           'aqsh':{'poytaxti':'washington',
                   'aholisi':'320 million',
                   'pul birligi':'dollar'}
           }
#for davlat,info in davlatlar.items():
    #if davlat.lower()=='aqsh':
        #davlat=davlat.upper()
    #else:
        #davlat=davlat.title()
    #print(f"\n{davlat} haqida malumotlar:")    
    #print(f"\n{davlat}ning poytaxti-{info['poytaxti'].title()}"
          #f"\n aholisi-{info['aholisi']}"
          #f"\n pul birligi - {info['pul birligi']}")
davlat=input("qaysi davlat haqida bilmoqchisiz ? :").lower()
if davlat in davlatlar:
        info=davlatlar[davlat]
        print(f"\n{davlat} haqida malumotlar:")    
        print(f"\n{davlat}ning poytaxti-{info['poytaxti'].title()}"
             f"\n aholisi-{info['aholisi']}"
             f"\n pul birligi - {info['pul birligi']}") 
else:    
         print(f"kechirasiz bizda {davlat} haqida malumot yuq")    


































