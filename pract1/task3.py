from datetime import datetime

while True:
    try:
        birth_year = int(input("Введіть рік Вашого народження: "))
        birth_month = int(input("Введіть місяць Вашого народження: "))
        birth_day = int(input("Введіть день Вашого народження: "))

        today = datetime.now()

        if birth_year > today.year:
            print("Ви ввели рік, який ще не настав. Введіть коректне значення.")
            continue

        age = today.year - birth_year

        if (today.month, today.day) < (birth_month, birth_day):
            age -= 1

        print(f"Ваш вік = {age}")
        break

    except ValueError:
        print("Помилка! Значення має бути цілим числом.")
