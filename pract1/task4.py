class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def display_info(self):
        print(f"{self.name}, {self.author}, {self.year}")


book1 = Book("Триста поезій", "Ліна Костенко", 2012)
book1.display_info()

book2 = Book("Тореадори з Васюківки", "Всеволод Нестайко", 1972)
book2.display_info()
