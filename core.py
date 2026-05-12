def correct_value():
    while True:
        value = input().strip()
        if value == "0" or value == "1":
            return int(value)
        else:
            print("Ошибка ввода! \nДопустимыезначения для ввода: Да - '1', Нет - '0' \nПопробуйте ещё раз")