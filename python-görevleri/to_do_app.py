yapilacaklar = []

while True:
  print("\nYapılacaklar Listesi:")
  if not yapilacaklar:
    print("Henüz bir görev eklenmedi.")
  else:
    for index, gorev in enumerate(yapilacaklar):
      print(f"{index+1}. {gorev['gorev']} (Tamamlandı: {gorev['tamamlandi']})")

  print("\nSeçenekler:")
  print("1. Yeni görev ekle")
  print("2. Görevi düzenle")
  print("3. Görevi tamamlandı olarak işaretle")
  print("4. Çıkış")

  secim = input("Seçiminizi yapın (1-4): ")

  if secim == "1":
    yeni_gorev = input("Yeni görevi girin: ")
    yapilacaklar.append({"gorev": yeni_gorev, "tamamlandi": False})
    print("Görev eklendi!")
  elif secim == "2":
    gorev_index = int(input("Düzenlemek istediğiniz görevin numarasını girin: ")) - 1
    if 0 <= gorev_index < len(yapilacaklar):
      yeni_gorev = input("Yeni görevi girin: ")
      yapilacaklar[gorev_index]["gorev"] = yeni_gorev
      print("Görev düzenlendi!")
    else:
      print("Geçersiz görev numarası.")
  elif secim == "3":
    gorev_index = int(input("Tamamlandı olarak işaretlemek istediğiniz görevin numarasını girin: ")) - 1
    if 0 <= gorev_index < len(yapilacaklar):
      yapilacaklar[gorev_index]["tamamlandi"] = True
      print("Görev tamamlandı olarak işaretlendi!")
    else:
      print("Geçersiz görev numarası.")
  elif secim == "4":
    print("Çıkış yapılıyor...")
    break
  else:
    print("Geçersiz seçim.")