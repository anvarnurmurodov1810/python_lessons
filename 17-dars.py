# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:22:56 2026

@author: User
"""

navoiy={'ism':'navoiy',
        'tyil':'1441',
        'manzil':'hirot',
        'asarlar':['xamsa','qush tili']}
bobur={'ism':'bobur',
       'tyil':'1483',
       'manzil':'samarqand',
       'asarlar':['boburnoma','hindiston']}
xorazmiy={'ism':'xorazm',
          'tyil':'780',
          'manzil':'xorazm',
          'asarlar':['algebra','hind raqamlari']}
mashhurlar=[navoiy,bobur,xorazmiy]
#for mashhur in mashhurlar:
    #print(f"\n{mashhur['ism'].title()} {mashhur['tyil']}-yilda {mashhur['manzil'].title()} da tug'ulgan")
#for mashhur in mashhurlar:
    #asarlar=mashhur['asarlar']
    #print(f"\n{mashhur['ism'].title()} ning mashhur asarlari:")
    #for asar in asarlar:
        #print(asar.title())

malumotlar={'abbos':['yulduzlar jangi 1','yulduzlar jangi 2','yulduzlar jangi 3'],
            'davron':['prestige','dexter','one piece'],
            'shoxjahon':['departed','breaking bad','prison break']}
#for ism,kinolar in malumotlar.items():
    #print(f"\n{ism.title()} ning sevimli kinolari:")
    #for kino in kinolar:
        #print(kino.title())
    
davlatlar={'uzbekistan':{'poytaxti':'toshkent',
                         'aholisi':'38 million',
                         'pul birligi':'sum'},
           'rossiya':{'poytaxti':'moskva',
                      'aholisi':'120 million',
                      'pul birligi':'rubl'},
           'amerika':{'poytaxti':'washington',
                      'aholisi':'320 million',
                      'pul birligi':'dollar'}
           }
#for davlat,info in davlatlar.items():
    #print(f"\n{davlat.title()} haqida malumotlar:")
    #print(f"poytaxti-{info['poytaxti'].title()} shahri ")
    #print(f"aholisi-{info['aholisi']}") 
    #print(f"pul birlig-{info['pul birligi']}")      
    
mamlakat=input("qaysi davlat haqida bilmoqchisiz ? :").lower()    
if mamlakat in davlatlar:
    info=davlatlar[mamlakat]
    print(f"{mamlakat.title()}ning poytaxti-{info['poytaxti'].title()}")
    print(f"aholisi-{info['aholisi']}")
    print(f"pul birligi-{info['pul birligi']}")
else:
    print(f"kechirasiz bizda {mamlakat.title()} haqida malumot yuq")

          



























