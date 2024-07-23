def menu():
    print("::menü::")
    print("1 - Ekleme")
    print("2 - Listeleme")
    print("3 - Arama")
    print("4 - Güncelleme")
    print("5 - Silme")
    print("6 - Çıkış")


def ekleme(personel):
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    telefon = input("Telefon: ")
    adres = input("Adres: ")
    eklenecek_veri = {
        "ad": ad,
        "soyad": soyad,
        "telefon": telefon,
        "adres": adres
    }
    personel.append(eklenecek_veri)
    print("Bilgiler eklendi..")


def listeleme(personel):
    print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO", "AD", "SOYAD", "TELEFON", "ADRES"))
    for i, kisi in enumerate(personel, 1):
        print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(i, kisi["ad"], kisi["soyad"], kisi["telefon"], kisi["adres"]))
    print("Listeleme bitti..")


def arama(personel):
    arama_ad = input("Aramak istediğiniz personel adı: ")
    print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO", "AD", "SOYAD", "TELEFON", "ADRES"))
    for i, kisi in enumerate(personel, 1):
        if arama_ad.lower() == kisi["ad"].lower():
            print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(i, kisi["ad"], kisi["soyad"], kisi["telefon"], kisi["adres"]))
            break
    else:
        print("Aradığınız kişi bulunamadı!")


def guncelleme(personel):
    arama_ad = input("Güncellemek istediğiniz personel adı: ")
    print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO", "AD", "SOYAD", "TELEFON", "ADRES"))
    found = []
    for i, kisi in enumerate(personel, 1):
        if arama_ad.lower() == kisi["ad"].lower():
            print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(i, kisi["ad"], kisi["soyad"], kisi["telefon"], kisi["adres"]))
            found.append(i - 1)

    if not found:
        print("Güncellemek istediğiniz kişi bulunamadı.")
    else:
        no = int(input("Güncellemek istediğiniz kişi no: ")) - 1
        if no in found:
            ad = input("Yeni ad: ")
            soyad = input("Yeni soyad: ")
            telefon = input("Yeni telefon: ")
            adres = input("Yeni adres: ")
            guncellenecek_veri = {
                "ad": ad,
                "soyad": soyad,
                "telefon": telefon,
                "adres": adres
            }
            personel[no] = guncellenecek_veri
            print("Değişiklikler eklendi...")
        else:
            print("Hatalı no değeri girildi..")


def silme(personel):
    arama_ad = input("Silmek istediğiniz personel adı: ")
    print("{:<5}{:<15}{:<15}{:<13}{:<25}".format("NO", "AD", "SOYAD", "TELEFON", "ADRES"))
    found = []
    for i, kisi in enumerate(personel, 1):
        if arama_ad.lower() == kisi["ad"].lower():
            print("{:<5}{:<15}{:<15}{:<13}{:<25}".format(i, kisi["ad"], kisi["soyad"], kisi["telefon"], kisi["adres"]))
            found.append(i - 1)

    if not found:
        print("Silmek istediğiniz kişi bulunamadı.")
    else:
        no = int(input("Silmek istediğiniz kişi no: ")) - 1
        if no in found:
            del personel[no]
            print("Personel bilgileri silindi..")
        else:
            print("Hatalı değer girildi..")


def main():
    personel = []

    while True:
        menu()
        secim = input("Seçiminiz: ")

        if secim == "6":
            print("Çıkılıyor....")
            break
        elif secim == "1":
            ekleme(personel)
        elif secim == "2":
            listeleme(personel)
        elif secim == "3":
            arama(personel)
        elif secim == "4":
            guncelleme(personel)
        elif secim == "5":
            silme(personel)
        else:
            print("Geçersiz seçim, tekrar deneyin.")


if __name__ == "__main__":
    main()
