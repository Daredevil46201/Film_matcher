def correct_value():
    while True:
        value = input("Ваш выбор (1/0):").lower().strip()
        if value == "0" or value == "1":
            return int(value)
        elif value == "стоп":
            print("Выбор остановлен")
            return None
        else:
            print("Ошибка ввода! \nДопустимыезначения для ввода: Да - '1', Нет - '0', Прекратить выбор - 'стоп' \nПопробуйте ещё раз")