print("Програма для виведення середнього арифметичного трьох чисел")

while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))
        res = (num1+num2+num3)/3
        print(f"Середнє арифметичне = {res:.2f}")
        break
    except ValueError:
        print("Помилка! Значення має бути числом")
