class Book:
    def __init__(self, name, author, year):
        if not name:
            raise ValueError("Назва не може бути порожньою")
        if not author:
            raise ValueError("Автор не може бути порожнім")
        if not isinstance(year, int) or year < 0 or year > 2026:
            raise ValueError("Некоректний рік")

        self.name = name
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Автор: {self.author}")
        print(f"Рік: {self.year}")


book1 = Book("Триста поезій", "Ліна Костенко", 2012)
book1.display_info()

book2 = Book("Тореадори з Васюківки", "Всеволод Нестайко", 1972)
book2.display_info()
