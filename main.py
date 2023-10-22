# Создаем пустой словарь для хранения заметок
notes = {}

# Функция для добавления заметки
def add_note():
    title = input("Введите название заметки: ")
    content = input("Введите текст заметки: ")
    notes[title] = content
    print("Заметка успешно добавлена!")

# Функция для удаления заметки
def delete_note():
    if not notes:
        print("Список заметок пуст.")
        return

    print("Список доступных заметок:")
    for title in notes.keys():
        print(title)

    title_to_delete = input("Введите название заметки для удаления: ")
    if title_to_delete in notes:
        del notes[title_to_delete]
        print("Заметка успешно удалена.")
    else:
        print("Заметка с таким названием не найдена.")

# Функция для вывода списка заметок
def list_notes():
    if not notes:
        print("Список заметок пуст.")
    else:
        print("Список заметок:")
        for title, content in notes.items():
            print(f"{title}: {content}")

# Функция для определения сезона по номеру месяца
def get_season(month):
    seasons = {
        12: ("зимы", "За окном падал белый снег"),
        1: ("зимы", "За окном падал белый снег"),
        2: ("зимы", "За окном падал белый снег"),
        3: ("весны", "Птицы пели прекрасные песни"),
        4: ("весны", "Птицы пели прекрасные песни"),
        5: ("весны", "Птицы пели прекрасные песни"),
        6: ("лета", "Солнце светило ярче чем когда-либо"),
        7: ("лета", "Солнце светило ярче чем когда-либо"),
        8: ("лета", "Солнце светило ярче чем когда-либо"),
        9: ("осени", "Урожай был невероятным"),
        10: ("осени", "Урожай был невероятным"),
        11: ("осени", "Урожай был невероятным"),
    }

    try:
        month = int(month)
        if month in seasons:
            season, description = seasons[month]
            return f"Вы родились в месяце {season}. {description}"
        else:
            return "Неверный номер месяца."
    except ValueError:
        return "Некорректный ввод. Введите номер месяца (1-12)."

# Главная функция приложения
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Удалить заметку")
        print("3. Вывести список заметок")
        print("4. Определить сезон по номеру месяца")
        print("5. Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            delete_note()
        elif choice == '3':
            list_notes()
        elif choice == '4':
            month = input("Введите номер месяца вашего рождения: ")
            season_info = get_season(month)
            print(season_info)
        elif choice == '5':
            print("Выход из приложения.")
            break
        else:
            print("Нет такой команды. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()
(2 ПРАКТИЧЕСКАЯ ДИСТАНЦИОНКА)