yaş = (input("75 yaşından ve büyük sigara bağımlısımısınız? : ")).strip().title()
kronik = (input("kronik rahatsızlığınız var mı? : ")).strip().title()
bağışıklık = (input("bağışıklık sitemi zayıf mı? : ")).strip().title()

risk = ((yaş == "Hayır") and (kronik == "Hayır") and (bağışıklık == "Hayır"))
if risk == False :
   print("Covid olmanız riskli!")
else:
  print("Covid sizin için riskli değil.")
