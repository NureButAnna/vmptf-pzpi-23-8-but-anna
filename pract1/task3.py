from datetime import datetime

while True:
    try:
        birth_year = int(input("Введіть рік вашого народження: "))
        today = datetime.now().year
        if birth_year > today:
            print("Ви ввели рік, який ще не настав. Введіть коректне значення.")
            continue
        age = today - birth_year
        print(f"Ваш вік = {age}")
        break
    except ValueError:
        print("Помилка! Значення має бути цілим числом.")
