def fibonacci(sinir):
    # İlk iki Fibonacci sayısını tanımlıyoruz.
    sayi1 = 0
    sayi2 = 1

    # İlk iki Fibonacci sayısını yazdırıyoruz.
    print(sayi1)
    print(sayi2)

    # Döngüyü başlatıyoruz. İlk iki sayı zaten yazdırıldığı için sinir-2 kadar dönüyoruz.
    for _ in range(sinir - 2):
        sayi3 = sayi1 + sayi2
        print(sayi3)
        # Sonraki adım için sayıları güncelliyoruz.
        sayi1 = sayi2
        sayi2 = sayi3

# Fonksiyonu çağırıyoruz. Örneğin, 10 Fibonacci sayısı üretmek için:
fibonacci(10)
