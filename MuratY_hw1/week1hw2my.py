
from xmlrpc.client import UNSUPPORTED_ENCODING, boolean


flag=True
while flag :

    name=input("Öğrencinin Adını giriniz: ").upper()
    surname=input("Öğrencinin Soyadını giriniz: ").upper()
    studnum=input("Öğrencinin Numarasını giriniz: ")
    lesson1=input("Birinci Ders Adını Giriniz:")
    les1mid=float(input("Bu dersin Vize Notunu giriniz: "))
    les1fin=float(input("Bu dersin Final Notunu giriniz: "))
    lesson2=input("İkinci Ders Adını Giriniz:")
    les2mid=float(input("Bu dersin Vize Notunu giriniz: "))
    les2fin=float(input("Bu dersin Final Notunu giriniz: "))
    lesson3=input("Üçüncü Ders Adını Giriniz:")
    les3mid=float(input("Bu dersin Vize Notunu giriniz: "))
    les3fin=float(input("Bu dersin Final Notunu giriniz: "))
    lesson4=input("Dördüncü Ders Adını Giriniz:")
    les4mid=float(input("Bu dersin Vize Notunu giriniz: "))
    les4fin=float(input("Bu dersin Final Notunu giriniz: "))

    kats1=0.4
    kats2=0.6
    puan=50
    print(f"{studnum} Nolu  {name} {surname}'in Ders Notları: ")

    if (les1mid*kats1 + les1fin*kats2) < puan:
        print(f"{lesson1} dersinden KALDI")
    else :
        print(f"{lesson1} dersinden GEÇTİ")
    if (les2mid*kats1 + les2fin*kats2) < puan:
        print(f"{lesson2} dersinden KALDI")
    else :
        print(f"{lesson2} dersinden GEÇTİ")
    if (les3mid*kats1 + les3fin*kats2) < puan:
        print(f"{lesson3} dersinden KALDI")
    else :
        print(f"{lesson3} dersinden GEÇTİ")
    if (les4mid*kats1 + les4fin*kats2) < puan:
        print(f"{lesson4} dersinden KALDI")
    else :
        print(f"{lesson4} dersinden GEÇTİ")


    secim=input("Yeni öğrenci için (D)evam, bitirmek için (T)amam basınız: ").upper()
    while True:
        if secim=="D":
            flag=True
            break
        elif secim=="T":
            flag=False
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Devam için D ye, Çıkmak için T ye basınız: ")
            secim=input("Yeni öğrenci için (D)evam, bitirmek için (T)amam basınız: ").upper()