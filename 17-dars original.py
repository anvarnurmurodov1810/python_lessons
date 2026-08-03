# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:15:58 2026

@author: User
"""

#savol=f"sevimli kitoblaringizni kiriting:"
#savol+="(sevimli kitoblaringizni kiritib bulgach 'exit' so'zini kiriting): "
#while True:
   # qiymat=input(savol)
  #  if qiymat=='exit':
 #       break
    
#print("dastur tugadi")    
   
savol="yoshingizni kiriting va chipta narxi qancha ekanligini biib oling \n(dasturni tugatmoqchi bulsangiz 'exit' yoki 'quit' deb yozing): "
while True:
    qiymat=input(savol)
    if qiymat=='quit' or qiymat=='exit':
        break
    yosh=int(qiymat)
    
    if yosh<7:
        chipta="2 ming so'm"
    elif yosh<18:
        chipta="3 ming so'm"
    elif yosh<65:
        chipta="10 ming so'm"
    else:
        chipta="tekin"
    
    print(f"siz uchun chipta narhi - {chipta}")    
        
print("dastur tugadi")    



































     