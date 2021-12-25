"""
Hesap Makinesi Programı
BTK - Sabah Grubu Öğrencileri İle Proje Geliştirme
"""
print("""HESAP MAKİNESİ\n1- TOPLAMA\n2- ÇIKARMA\n3- ÇARPMA\n4- BÖLME \n Çıkmak İstedeğinizde x'e basınız""")
while True:
    secenek = input("Lütfen bir seçim yapınız:").lower()
    if secenek == "x":
        print("İşleminiz sonlandırılıyor Lütfen Bekleyiniz")
        break
    elif secenek=="1":
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        print("Sayılarınızın toplamı: ",sayi1+sayi2)
    elif secenek=="2":
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        print("Sayılarınızın farkı: ",sayi1-sayi2)
    elif secenek=="3":
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        print("Sayılarınızın çarpımı: ",sayi1*sayi2)
    elif secenek=="4":
        sayi1 = int(input("1. sayıyı giriniz:"))
        sayi2 = int(input("2. sayıyı giriniz:"))
        try:
            print("Sayıların Bölümü:", sayi1/sayi2)
        except ZeroDivisionError:
            print("Nerede Hata Yaptığınızı öğrenmek istiyorsanız Evet istemiyorsanız Hayır yazınız")
            istek = input("İsteğinizi Yazınız:").lower()
            if istek == "evet":
                print("Bir Sayıyı 0'a bölemezsiniz")
            else:
                continue
    else:
        print("Lütfen 1-4 arası bir seçim yapınız!")

