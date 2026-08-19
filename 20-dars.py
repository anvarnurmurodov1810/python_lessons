# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:18:35 2026

@author: User
"""

#def mijoz_info(ism, familiya, tyil, tjoy, email='', tel=None):
    #"""foydalnuvchi haqidagi malumotlarni lug'at ko'rinishida saqlovchi funkisya"""
   # mijoz={'ism':ism,
     #      'familiya':familiya,
    #       'tyil':tyil,
   #        'tjoy':tjoy,
  #         'email':email,
  #         'telefon':tel}
 #   return mijoz

#print("foydalanuvchi haqidagi ma'lumotlarni kiriting: ")
#mijozlar=[]
#while True:
#    ism=input("ismi:")
    #familiya=input("familiyasi:")
   # tyil=input("tugulgan yili:")
  #  tjoy=input("tug'ulgan joyi:")
 #   email=input("emaili:")
#    telefon=input('telefon raqami:')
    #mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
   # savol=input("yangi mijoz qo'shasizmi ? (ha/yuq)")
  #  if savol!="ha":
 #       break
    
#for mijoz in mijozlar:
#    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}")
#    print(f"{mijoz['tyil']} yoshda telefon raqami-{mijoz['telefon']}")    

#def katta_sonni_aniqlash(x,y,z):
  #  """uchta sondan kattasini aniqlash"""
  #  if x>y and x>z:
  #      print(x)
  #  elif y>x and y>z:
  #      print(y)
 #   else:
#        print(z)

#katta_sonni_aniqlash(5,623,-9)

#def aylana_haqida(radius,pi=3.141582):
#    """aylana haqida"""
#    aylana={'radiusi':radius,
#            'dieametri':2*radius,
#            'uzunligi':2*pi*radius,
#            'yuzasi':pi*radius**2}
#    print(aylana)
#    return aylana
#aylana_haqida(3)

#def tub_sonni_topish(min,max):
    
   # tub_sonlar=[]
  #  for n in range(min,max+1):
 #       tub=True
#        if (n==1):
         #   tub=False
        #elif (n==2):
       #     tub=True
      #  else:
     #       for x in range(2,n):
    #            if (n%x==0):
   #                 tub=False
  #      if tub:
 #           tub_sonlar.append(n)
#            
#    print(tub_sonlar)    
#    return tub_sonlar
            
#tub_sonni_topish(5,57)        
                    
def febanachi(n):
    sonlar=[]
    for x in range(n):
        if x==1 or x==0:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
print(febanachi(20))        
        



















