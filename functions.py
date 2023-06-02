def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find))


def search(book: list[str], info: str) -> str | None:
    """Находит в списке записи по определенному критерию поиска"""
    res = []
    for line in book:
        if info in line:
            res.append(line)
    if len(res) == 0:
        print("Информация не была найдена")
    elif len(res) == 1:
        return res[0]
    else:
        print()
        info = input('''Найдено несколько результатов, относящихся к вашему запросу.
                     \rПожалуйста, укажите ваш запрос: ''')
        return search(res, info)

def change_data():
    """Редактирует выбранную пользователем запись в списке"""
    book = open_file_to_read('book.txt')
    if not book:
        return
    note_to_edit = input("\nВведите заметку, которую вы хотели бы отредактировать: ")
    found_note = search(book, note_to_edit)
    if not found_note:
        return
    indx = book.index(found_note)
    fio, phone_num = found_note.split(' | ')
    new_fio = input("Введите новыe ФИО. Если вы хотите оставить все как есть, нажмите Enter.': ")
    if new_fio == '':
        new_fio = fio
    new_phone_num = input("Введите новый номер телефона. Если вы хотите оставить все как есть, нажмите Enter.': ")
    new_phone_num = phone_num if new_phone_num == '' else new_phone_num + '\n'
    book[indx] = f'{new_fio.rjust(30)} | {new_phone_num}'
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(book))
    print('Изменения были сохранены.')

def open_file_to_read(file_name: str) -> list[str] | None:
    """
    Открывает файл для чтения и возращает его содержимое в виде списка строк.
    Если файл не существует, сообщает об этом в консоль и возвращает 'None'
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print("Файл не существует")

def delete_data() -> None:
    """Удаляет выбранную заметку"""
    book = open_file_to_read('book.txt')
    if not book:
        return
    note_to_edit = input("\nВведите заметку, которую вы хотели бы удалить: ")
    found_note = search(book, note_to_edit)
    if not found_note:
        return
    book.remove(found_note)
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(book))
    print('Заметка была удалена.')