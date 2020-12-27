#!/usr/bin/env python

print("""
---------------------------------------------------------------
--                                                                 -
--                    HOŞ GELDİNİZ                        --
-             BAŞLAMAK İÇİN LÜTFEN BELİRTİLEN-                               ADIMLARI YERİNE GETİRİN                                                                               -
--------------------------------------------------------------
""")
print("\n""BAŞLAMAK İÇİN LÜTFEN KAYIT OLUN.""\n""KAYIT OLMAK İÇİN LÜTFEN 1 i SEÇİNİZ.")
while True:
              e=input("\n""\n""1-) Kayıt Ol""\n"":")
              if e=="1":
                  print("\n")
                  break
              else:
                	print("\n""Hatalı Seçim")


while True:
                a=input("\n""Ad Soyad    :")
                b=input("\n""Password     :")
                d=input("\n""Onay Password    :")
                if b==d:
                     print("\n""Hesabınız Başarıyla Oluşturuldu.")
                     print("\n""\n""\n""\t""\t""Hoş Geldin",a)
                     break
                else:
                   	print("\n""Şifreler Eşleşmiyor.")
                   	
input("\n""\n""Başlamak İçin Herhangi Bir Tuşa Basın.""\n""\n""\n""___________________________________________________________""\n""\n")
                   	
                   	              
print("""         
            ========Bilgi=======
Bilmediğin Soruya [pas] Deyip geçebilirsin""")
print("""__________________________________________________________""")
 
print("\n""\n""HARFLER""\t""\t""\t""\t""YAZILIŞI & ""\n""\t""\t""\t""\t""OKUNUŞU")
while True:
	            a=input("\n""a""\t""\t""\t""\t"":")
	            b=input("\t""\t""\t""\t"":")
	            if a=="a" and b=="ey":
	            	print()
	            	break
	            elif a=="pas":
	            	print("\n""Malesef Doğru cvp: a-ey")
	            	break
	            elif b=="pas":
	            	print("\n""Malesef Doğru cvp: a-ey")
	            	break
	            else:
	            	print("\t""\t""\t""\t""YANLIŞ")
	            	
	            	
while True:
	            a=input("b""\t""\t""\t""\t"":")
	            b=input("\t""\t""\t""\t"":")
	            if a=="b" and b=="be":
	            	print()
	            	break
	            elif a=="pas":
	            	print("\n""Malesef Doğru cvp: b-be")
	            	break
	            elif b=="pas":
	            	print("\n""Malesef Doğru cvp: b-be")
	            	break
	            else:
	            	print("\t""\t""\t""\t""YANLIŞ")
	            	