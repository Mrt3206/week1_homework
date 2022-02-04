flag=True    
while flag:
    
    boy=int(input("Lütfen boyunuzu (cm olarak) giriniz: "))
    kilo=int(input("Lütfen Kilonuzu (kg)giriniz: "))

    beden_kitle_indeksi=kilo/((boy/100)**2)

    if beden_kitle_indeksi<25:
        print("NORMAL :)\n\n")
    elif 25 <= beden_kitle_indeksi < 30:
        print("FAZLA KİLOLU!\n\n")
    elif 30 <= beden_kitle_indeksi <40:
        print("OBEZ!!\n\n")
    elif beden_kitle_indeksi>=40:
        print("AŞIRI ŞİŞMAN!!!\n\n")
    else:
        print("Bir hata oluştu.")
    
    secim=input("(D)evam mı,  (T)amam mı : ").upper()
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
            secim=input("(D)evam mı,  (T)amam mı : ").upper()  
