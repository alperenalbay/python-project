import random


def get_random_word():
    words = ["python", "developer", "hangman", "programming", "computer"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def hangman():
    word = get_random_word()
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6

    print("Adam Asmaca oyununa hoş geldiniz!")
    while wrong_attempts < max_attempts:
        print("\nKelime: ", display_word(word, guessed_letters))
        guess = input("Bir harf tahmin edin: ").lower()

        if guess in guessed_letters:
            print("Bu harfi zaten tahmin ettiniz.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Doğru tahmin!")
        else:
            wrong_attempts += 1
            print(f"Yanlış tahmin! Kalan hak: {max_attempts - wrong_attempts}")
            print("Adam:", "O" if wrong_attempts > 0 else " ", "|\n" if wrong_attempts > 1 else " ",
                  "/|\\" if wrong_attempts > 2 else " ", "/ \\" if wrong_attempts > 4 else " ")

        if all(letter in guessed_letters for letter in word):
            print("\nTebrikler! Kelimeyi doğru tahmin ettiniz: ", word)
            break
    else:
        print("\nÜzgünüz, kaybettiniz. Doğru kelime: ", word)


hangman()
