# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:52:21 2026

@author: User
"""

#def yosh_hisoblash(ism, tugulgan_yil,joriy_yil=2026) :
  #  """foydalanuvchining yoshini hisoblaydigan funksiya"""
  #  print(f"{ism.title()} {joriy_yil-tugulgan_yil} yoshdasiz")
 #   
#yosh_hisoblash('anvar',2008)    
    
#def kvadrat_kub(son):
  #  """sonning kvadrati va kubini hisoblaydigan funksiya"""
 #   print(f"{son} ning kvadrati={son**2}",
#          f"\n{son} ning kubi={son**3}")
 #   
#kvadrat_kub(75)    

#def juft_toqni_hisoblash(son):
#    """sonning juft yoki toqligini aniqlaydigan dastur"""
#    if son%2==0:
#        print(f"{son} soni-juft")
#    else:
#        print(f"{son} soni-toq")
#        
#juft_toqni_hisoblash(11)

#def katta_son(son1,son2):
#    """katta sonni aniqlaydigan funksiya"""
#    if son1>son2:
#        print(son1)
#    elif son1<son2:
#        print(son2)
#    else:
#        print(f"{son1}={son2}")
#
#katta_son(82,102)        

#def son_daraja(x,y=2):
  # """sonning darajasini hisoblaydigan dastur"""
 #  print(f"{x**y}")
    
#son_daraja(x=7)    
def sonning_ekubi(x):
    """sonning buluvchilarini topish"""
    for n in range(2,11):
        if x%n==0:
            print(f"{n} soni {x}ga qoldiqsiz bulinadi")
            
sonning_ekubi(40)            































