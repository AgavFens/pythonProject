import math
def main():
    print("Инженерный калькулятор")
    while True:
        print("Доступные операции:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("11. Выход")

        choice = input("Выберите операцию (1/2/3/4/5/6/7/8/9/10/11): ")

        if choice == '11':
            print("Пока.")
            break

        if choice not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'):
            print("только с 1 до 11, дальше пути нет")
            continue

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("ЧИСЛА ВВОДИ!!!")
                continue

        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 == 0:
                print("Ошибка: деление на ноль")
                continue
            result = num1 / num2
        elif choice == '5':
            result = num1 ** num2
        elif choice == '6':
            if num1 < 0:
                print("Ошибка: нельзя извлекать корень из отрицательного числа")
                continue
            result = math.sqrt(num1)
        elif choice == '7':
            if num1 < 0:
                print("Ошибка: факториал определен только для неотрицательных целых чисел")
                continue
            result = math.factorial(int(num1))
        elif choice == '8':
            result = math.sin(num1)
        elif choice == '9':
            result = math.cos(num1)
        elif choice == '10':
            result = math.tan(num1)

        print("Результат: {}".format(result))


if __name__ == "__main__":
    main()
