plyr1= input("Lütfen 1.oyuncunun ismini giriniz: ").upper()
plyr2=input("Lütfen 2.oyuncunun ismini giriniz: ").upper()
oyun=int(input("Kaç oyun oynacaksınız: "))
plyr1_puan=0
plyr2_puan=0
oyunsayisi=1
print("Taş, Kağıt, Makas")
while oyunsayisi <=oyun :
    secim_plyr1=input(f"{plyr1}  Seçiminizi yazınız: ").upper()
    secim_plyr2=input(f"{plyr2}  Seçiminizi yazınız: ").upper()

    if secim_plyr1=="TAŞ" or secim_plyr1=="TAS" :
        if secim_plyr2=="KAĞIT" or secim_plyr2== "KAGIT":
            print(f"{plyr2} kazandınız.")
            plyr2_puan+=1
            oyunsayisi+=1
        elif secim_plyr2=="MAKAS" :
            print(f"{plyr1} kazandınız.")
            plyr1_puan+=1
            oyunsayisi+=1
        elif secim_plyr2=="TAŞ" or secim_plyr2=="TAS" :
            print("Beraberlik")
            oyunsayisi+=1
        else :
            print("Lütfen Seçiminizi düzgün giriniz: ")
            
    
    elif secim_plyr1=="KAĞIT" or secim_plyr1=="KAGIT" :
        if secim_plyr2=="KAĞIT" or secim_plyr2== "KAGIT":
            print("Beraberlik")
            oyunsayisi+=1
        elif secim_plyr2=="MAKAS" :
            print(f"{plyr2} kazandınız.")
            plyr2_puan+=1   
            oyunsayisi+=1 
        elif secim_plyr2=="TAŞ" or secim_plyr2=="TAS" :
            print(f"{plyr1} kazandınız.")
            plyr1_puan+=1
            oyunsayisi+=1
        else :
            print("Lütfen Seçiminizi düzgün giriniz: ")    
    elif secim_plyr1=="MAKAS":
        if secim_plyr2=="KAĞIT" or secim_plyr2== "KAGIT":
            print(f"{plyr1} kazandınız.")
            plyr1_puan+=1
            oyunsayisi+=1
        elif secim_plyr2=="MAKAS" :
            print("Beraberlik")
            oyunsayisi+=1
        elif secim_plyr2=="TAŞ" or secim_plyr2=="TAS" :
            print(f"{plyr2} kazandınız.")
            plyr2_puan+=1
            oyunsayisi+=1
        else :
            print("Lütfen Seçiminizi düzgün giriniz: ")
              
    else:
        print("Lütfen Seçiminizi düzgün giriniz: ")
        
    if oyunsayisi <= oyun+1 :
        print(f"{oyunsayisi-1}. Sonundaki Puan Durumu: ")
        print(f"Puan Durumu {plyr1} = {plyr1_puan}")
        print(f"Puan Durumu {plyr2} = {plyr2_puan}")
    
    if oyunsayisi == (oyun+1):
        if plyr1_puan>plyr2_puan :
            print(f"Tebrikler {plyr1} Kazandınız ")
            print(f"Puan Durumu {plyr1} = {plyr1_puan}")
            print(f"Puan Durumu {plyr2} = {plyr2_puan}")
        
        elif plyr1_puan< plyr2_puan:
            print(f"Tebrikler {plyr2} Kazandınız ")
            print(f"Puan Durumu {plyr1} = {plyr1_puan}")
            print(f"Puan Durumu {plyr2} = {plyr2_puan}")
        else :
            print("Tebrikler berabere ")
            print(f"Puan Durumu {plyr1} = {plyr1_puan}")
            print(f"Puan Durumu {plyr2} = {plyr2_puan}")
      
    
    