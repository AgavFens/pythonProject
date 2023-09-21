def rectangle_area(width, height):
    area = width * height
    return area

width = int(input())
height = int(input())
area = rectangle_area(width, height)
print("Площадь прямоугольника:", area)

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input())
result = is_even(number)
if result:
    print(number, "является четным числом.")
else:
    print(number, "является нечетным числом.")


    def sum_digits(number):
        total = 0

        number_str = str(number)

        for digit_str in number_str:
            digit = int(digit_str)
            total += digit

        return total

    number = int(input())
    result = sum_digits(number)
    print("Сумма цифр числа", number, "равна", result)