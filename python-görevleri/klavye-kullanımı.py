
sol = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b'}
sağ = {'y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm'}
word = input('Kelime giriniz:')
kelime = ((set(word) & left) != set() and  (set(word) & right) != set())
print(kelime)
if kelime == True :
  print(Girmiş olduğunuz kelimeye göre rahatça on parmak klavye kullanabilirsiniz)
else:
  print(Girmiş olduğunuz kelimeye göre sağ yada sol parmaklarınızla klavye kullanbiliyorsunuz)
