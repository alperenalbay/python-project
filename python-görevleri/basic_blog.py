class BlogPost:
    def __init__(self, title, content, category):
        self.title = title
        self.content = content
        self.category = category

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self):
        title = input("Başlık: ").strip()
        content = input("İçerik: ").strip()
        category = input("Kategori: ").strip()
        post = BlogPost(title, content, category)
        self.posts.append(post)
        print(f"'{title}' başlıklı yazı eklendi.")

    def list_posts(self):
        if not self.posts:
            print("Henüz yazı eklenmemiş.")
        else:
            for i, post in enumerate(self.posts):
                print(f"{i + 1}. {post.title} - {post.category}")

    def view_post(self):
        post_number = int(input("Görüntülemek istediğiniz yazının numarasını girin: "))
        if 0 < post_number <= len(self.posts):
            post = self.posts[post_number - 1]
            print(f"\nBaşlık: {post.title}")
            print(f"Kategori: {post.category}")
            print(f"İçerik: {post.content}\n")
        else:
            print("Geçersiz numara. Lütfen tekrar deneyin.")

    def delete_post(self):
        post_number = int(input("Silmek istediğiniz yazının numarasını girin: "))
        if 0 < post_number <= len(self.posts):
            post = self.posts.pop(post_number - 1)
            print(f"'{post.title}' başlıklı yazı silindi.")
        else:
            print("Geçersiz numara. Lütfen tekrar deneyin.")

def main():
    blog = Blog()
    while True:
        print("\nBasit Blog Uygulaması")
        print("1. Yeni Yazı Ekle")
        print("2. Yazıları Listele")
        print("3. Yazı Görüntüle")
        print("4. Yazı Sil")
        print("5. Çıkış")
        choice = input("Seçiminiz: ").strip()

        if choice == '1':
            blog.add_post()
        elif choice == '2':
            blog.list_posts()
        elif choice == '3':
            blog.view_post()
        elif choice == '4':
            blog.delete_post()
        elif choice == '5':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
