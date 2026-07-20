# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:38:03 2026

@author: Anvar Nurmurodov
"""

#otam={"ism":"Fazlidddin","tug'ilgan_yil":"1979","yashash_manzili":"Toshkent"}
#tyil=otam["tug'ilgan_yil"]
#manzil=otam["yashash_manzili"]
#print(f"otamning ismi {otam['ism'].title()},{tyil}-yilda tug'ilgan,{manzil} shahrida yashaydi")

#taomlar={"otam":"shashlik","onam":"somsa","akam":"barak","opam":"manti","men":"osh"}
#taom_1=taomlar['otam']
#print(f"otamning sevimli taomi {taom_1}")
#taom_2=taomlar['onam']
#print(f"onamning sevimli taomi {taom_2}")
#taom_3=taomlar["akam"]
#print(f"akamning sevimli taomi {taom_3}")

python_izohli_lugati={
       'integer':'butun son',
       'float':"o'nlik son",
       'string':'matn',
       'list':"ro'yxat",
       'tuple':"o'zgarmas ro'yxat"}
kalit=input("kalit so'zni kiriting:").lower()
#print(python_izohli_lugati.get(kalit,"bunday so'z mavjud emas"))
tarjima=python_izohli_lugati.get(kalit)
if tarjima==None:
    print("bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")    

















