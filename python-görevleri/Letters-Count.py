def cümle(str1):
    frekans = {}
    for karakter in str1:
        if karakter in frekans:
            frekans[karakter] += 1
        else:
            frekans[karakter] = 1
    return frekans

print(cümle(input("Cümleyi giriniz: ")))
