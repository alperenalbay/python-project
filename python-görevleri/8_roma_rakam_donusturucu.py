def intToRoman(num):
  values = [
    1000, 900, 500, 400,
    100, 90, 50, 40,
    10, 9, 5, 4,
    1
  ]
  roman_values = [
    "M", "CM", "D", "CD",
    "C", "XC", "L", "XL",
    "X", "IX", "V", "IV",
    "I"
  ]
  roman_number = ''
  i = 0
  while num > 0:
    for _ in range(num // values[i]):
      roman_number += roman_values[i]
      num -= values[i]
    i += 1
  return roman_number

sayi = int(input("Bir sayı girin: "))
roman_sayi = intToRoman(sayi)
print(f"{sayi} sayısının Roma rakamı karşılığı: {roman_sayi}")