class Recipe:
    def __init__(self, name, ingredients, instructions, category):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category

class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.categories = {}

    def add_recipe(self):
        name = input("Tarif adı: ").strip()
        ingredients = input("Malzemeler (virgülle ayrılmış): ").strip().split(',')
        instructions = input("Talimatlar: ").strip()
        category = input("Kategori: ").strip()
        
        recipe = Recipe(name, ingredients, instructions, category)
        self.recipes.append(recipe)
        
        if category in self.categories:
            self.categories[category].append(recipe)
        else:
            self.categories[category] = [recipe]
        
        print(f"'{name}' adlı tarif eklendi.")
    
    def list_recipes(self):
        if not self.recipes:
            print("Henüz tarif eklenmemiş.")
        else:
            for i, recipe in enumerate(self.recipes):
                print(f"{i + 1}. {recipe.name} ({recipe.category})")

    def list_categories(self):
        if not self.categories:
            print("Henüz kategori eklenmemiş.")
        else:
            for category, recipes in self.categories.items():
                print(f"{category}: {len(recipes)} tarif")
    
    def view_recipe(self):
        name = input("Görüntülemek istediğiniz tarifin adı: ").strip()
        found = False
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                print(f"\nTarif: {recipe.name}")
                print(f"Malzemeler: {', '.join(recipe.ingredients)}")
                print(f"Talimatlar: {recipe.instructions}")
                print(f"Kategori: {recipe.category}\n")
                found = True
                break
        if not found:
            print(f"'{name}' adlı tarif bulunamadı.")

def main():
    recipe_book = RecipeBook()
    while True:
        print("\nYemek Tarifleri Uygulaması")
        print("1. Tarif Ekle")
        print("2. Tarifleri Listele")
        print("3. Kategorileri Listele")
        print("4. Tarifi Görüntüle")
        print("5. Çıkış")
        choice = input("Seçiminiz: ").strip()

        if choice == '1':
            recipe_book.add_recipe()
        elif choice == '2':
            recipe_book.list_recipes()
        elif choice == '3':
            recipe_book.list_categories()
        elif choice == '4':
            recipe_book.view_recipe()
        elif choice == '5':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
