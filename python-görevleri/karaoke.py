import time

# Şarkı sözleri ve zamanlamaları (saniye cinsinden)
lyrics = [
    (0, "Bu gece son"),
    (2, "Bu gece seninle son"),
    (4, "İçimde bir hüzün var"),
    (6, "Bu gece son")
]

def display_lyrics(lyrics):
    print("Şarkı başlıyor...")
    start_time = time.time()
    for timestamp, line in lyrics:
        while time.time() - start_time < timestamp:
            time.sleep(0.1)  # Zamanlamayı kontrol etmek için bekleme
        print(line)

def main():
    print("Basit Karaoke Uygulaması")
    print("Şarkı seçildi: Bu Gece Son")
    display_lyrics(lyrics)
    print("Şarkı bitti. Teşekkürler!")

if __name__ == "__main__":
    main()
