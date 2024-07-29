import json

def load_dictionary(file_name="dictionary.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_dictionary(dictionary, file_name="dictionary.json"):
    with open(file_name, "w") as file:
        json.dump(dictionary, file)

def add_word(dictionary):
    word = input("Eklemek istediğiniz kelime: ").strip()
    meaning = input(f"{word} kelimesinin anlamı: ").strip()
    dictionary[word] = meaning
    print(f"{word} kelimesi eklendi.")

def search_word(dictionary):
    word = input("Aramak istediğiniz kelime: ").strip()
    if word in dictionary:
        print(f"{word} kelimesinin anlamı: {dictionary[word]}")
    else:
        print(f"{word} kelimesi sözlükte bulunamadı.")

def delete_word(dictionary):
    word = input("Silmek istediğiniz kelime: ").strip()
    if word in dictionary:
        del dictionary[word]
        print(f"{word} kelimesi silindi.")
    else:
        print(f"{word} kelimesi sözlükte bulunamadı.")

def list_words(dictionary):
    if dictionary:
        for word, meaning in dictionary.items():
            print(f"{word}: {meaning}")
    else:
        print("Sözlükte henüz hiç kelime yok.")

def main():
    dictionary = load_dictionary()
    while True:
        print("\nSözlük Uygulaması")
        print("1. Kelime Ekle")
        print("2. Kelime Ara")
        print("3. Kelime Sil")
        print("4. Tüm Kelimeleri Listele")
        print("5. Çıkış")
        choice = input("Seçiminiz: ").strip()

        if choice == '1':
            add_word(dictionary)
        elif choice == '2':
            search_word(dictionary)
        elif choice == '3':
            delete_word(dictionary)
        elif choice == '4':
            list_words(dictionary)
        elif choice == '5':
            save_dictionary(dictionary)
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
