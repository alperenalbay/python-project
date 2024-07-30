def introduction():
    print("Bir ormanın derinliklerinde kayboldun.")
    print("Önünde iki yol var: biri sağa, diğeri sola gidiyor.")
    print("Hangi yoldan gitmek istersin?")
    choice = input("Sağa gitmek için 'sağ', sola gitmek için 'sol' yaz: ").lower()
    if choice == "sağ":
        right_path()
    elif choice == "sol":
        left_path()
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        introduction()

def right_path():
    print("Sağa gittin ve karanlık bir mağaraya ulaştın.")
    print("İçeri girmek mi istiyorsun yoksa geri dönmek mi?")
    choice = input("Girmek için 'gir', geri dönmek için 'dön' yaz: ").lower()
    if choice == "gir":
        print("Mağaraya girdin ve bir hazine buldun! Kazandın!")
    elif choice == "dön":
        print("Geri döndün ve güvenli bir şekilde ormandan çıktın. Macera sona erdi.")
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        right_path()

def left_path():
    print("Sola gittin ve bir nehirle karşılaştın.")
    print("Nehri geçmek mi yoksa geri dönmek mi istiyorsun?")
    choice = input("Geçmek için 'geç', geri dönmek için 'dön' yaz: ").lower()
    if choice == "geç":
        print("Nehri geçtin ve bir ejderha tarafından yakalandın. Kaybettin.")
    elif choice == "dön":
        print("Geri döndün ve güvenli bir şekilde ormandan çıktın. Macera sona erdi.")
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        left_path()

def main():
    print("Metin Tabanlı Macera Oyunu")
    introduction()

if __name__ == "__main__":
    main()
