

menu: list[str] = [          # переменная для работы с пунктами основного меню
    'открыть файл',
    'сохранить файл',
    'показать все контакты',
    'создать контакт',
    'найти контакт',
    'изменить контакт',
    'удалить контакт',
    'выход'
]

global_phone_book: dict[int,dict[str,str]] = {}  # глобальная переменная, размещает справочник на время работы с ним
wrong_input: int = 0 # переменная для выхода из цикла wile

def next_id(phone_book) -> int:
    """
    Функция следующего свободного id в справочнике
    """
    if phone_book:
        return max(phone_book) + 1
    return 1


def pause() -> None:
    """
     Функция паузы для удобства чтения вывода данных
     """
    input('Нажмите "ввод" для выхода в основное меню')


def phone_open() -> dict[int,dict[str,str]]:
    """
     Функция открытия файла и запись данных в глобальную переменную global_phone_book
     """
    with open('phone_book.txt', 'r', encoding='UTF-8') as file:
        data: list[str]= sorted(file.readlines(), key=lambda x: x[0])
        data: list[list[str]] = list(map(lambda x: x.strip().split(';'), data))
        for contact in data:
            global_phone_book[next_id(global_phone_book)] = {'name': contact[0], 'phone': contact[1],
                                                             'comment': contact[2]}
        if global_phone_book:
            print('Телефонная книга успешно открыта')
        else:
            print('Телефонная книга пуста')
        return global_phone_book


def phone_show(phone_book, stop=True) -> None:
    """
     Функция печати справочника либо отдельный контактов
     """
    if phone_book:
        print('=' * 66)
        for user_id, contact in phone_book.items():
            print(f'{user_id: >2}. {contact['name']: <20} {contact['phone']: <20} {contact['comment']: <20}')
        print('=' * 66)
        if stop:
            pause()

    else:
        print('Телефонная книга не открыта, выберите пункт "открыть файл"')


def phone_create() -> None:
    """
     Функция создания контакта и добавления его в global_phone_book
     """
    if global_phone_book:
        contact: dict[str,str] = {}    # переменная для временного хранения создаваемого контакта
        fields: dict[str,str] = {'name': 'Введите имя: ', 'phone': 'Введите телефон: ', 'comment': 'Введите комментарий: '} # переменная для подменю ввода
        for key, field in fields.items():
            contact[key] = input(field)
        user_id: int = next_id(global_phone_book)
        global_phone_book[user_id] = contact
        print('Успешно создан новый контакт:')
        print(f'{user_id: >2}. {contact['name']: <20} {contact['phone']: <20} {contact['comment']: <20} ')
        print('не забудьте сохранить файл перед выходом')
    else:
        print('Телефонная книга не открыта, выберите пункт "открыть файл"')
    pause()


def phone_save() -> None:
    """
     Функция записи глобальной переменной global_phone_book в файл
     """
    data: list[str] =[]
    for contact in global_phone_book.values():
        data.append(';'.join(contact.values()))
    data: str = '\n'.join(data)
    with open('phone_book.txt', 'w', encoding='UTF-8') as file:
        file.write(data)
    print('Контакт успешно сохранен')


def phone_find() -> None:
    """
     Функция поиска во всех полях global_phone_book по ключевому слову
     """
    result: dict[int,dict[str,str]] = {}
    key_word: str = input('Введите слово для поиска: ')
    for user_id, contact in global_phone_book.items():
        for key, field in contact.items():
            if key == 'phone':
                res: list[str] = []
                for i in field:
                    if i.isdigit():
                        res.append(i)
                field: str = ''.join(res)
            if key_word.lower() in field.lower():
                result[user_id] = contact
                break
    if result:
        phone_show(result)
    else:
        print('Контакт не найден')
        pause()


def phone_change() -> None:
    """
     Функция изменения контакта с выбором поля для изменения
     """
    menu_change: dict[str,str] = {'Имя': 'name', 'Телефон': 'phone', 'Комментарий': 'comment', 'Выход': None} # переменная меню
    contact_change: dict[int,dict[str,str]] = {}                     # переменная для временного хранения и изменения выбранного контакта
    wrong_input_change: int = 0    # переменная для выхода из wile
    user_id_choice: str = input('Введите порядковый номер контакта который хотите изменить: ')
    if user_id_choice.isdigit() and 0 < int(user_id_choice) < next_id(global_phone_book):
        contact_change[int(user_id_choice)] = global_phone_book[int(user_id_choice)]
        phone_show(contact_change, False)
        while wrong_input_change < 5:
            for i, item in enumerate(menu_change, 1):
                print(f'\t {i}. {item}')
            field_id: str = input("Введите номер поля которое хотите изменить: ")
            if field_id.isdigit() and 0 < int(field_id) < 4:
                wrong_input_change=0
                global_phone_book[int(user_id_choice)][list(menu_change.values())[int(field_id) - 1]] = input(
                    f'Введите {list(menu_change.keys())[int(field_id) - 1]}: ')
                contact_change[int(user_id_choice)] = global_phone_book[int(user_id_choice)]
                phone_show(contact_change, False)
            elif field_id.isdigit() and int(field_id) == 4:
                break
            else:
                print("Введён неверный символ")
                wrong_input_change += 1
    elif user_id_choice.isdigit():
        print(f'Контакта с порядковым номером {user_id_choice} не существует')
    else:
        print("Введён неверный символ")
    pause()


def phone_delete() -> None:
    """
      Функция удаления контакта
      """
    contact_del: dict[int,dict[str,str]] = {}  # переменная вывода выбранного контакта для дополнительного запрос на удаление
    del_id: str = input('Введите порядковый номер контакта который хотите удалить: ')
    if del_id.isdigit() and 0 < int(del_id) < next_id(global_phone_book):
        contact_del[int(del_id)] = global_phone_book[int(del_id)]
        print('Вы действительно хотите удалить контакт: ')
        phone_show(contact_del, False)
        con_del_id: str= input('Если да введите "Y": ')
        if con_del_id == 'Y' or con_del_id == 'y':
            print('Контакта удалён')
            del global_phone_book[int(del_id)]
    elif del_id.isdigit() and not 0 < int(del_id) < next_id(global_phone_book):
        print(f'Контакта с порядковым номером {del_id} не существует')
    else:
        print('Введён не верный символ')
    pause()

def phone_out() -> None:
    """
      Функция выхода из программы
      """
    key: str = input('Введите "Y" что бы сохранить файл: ')
    if key=='Y' or key=='y' and global_phone_book:
        phone_save()
    else:
        print("Телефонная книга пуста или не отрывалась")
        print("сохранение не выполнено")


while wrong_input < 5: # цикл с основным меню
    print('Основное меню')
    for i, item in enumerate(menu, 1):
        print(f'\t {i}. {item}')
    user_key = input('Введите номер пункта меню (1-8): ')
    if user_key == '1':
        wrong_input=0
        phone_open()
    elif user_key == '2':
        wrong_input=0
        phone_save()
    elif user_key == '3':
        wrong_input=0
        phone_show(global_phone_book)
    elif user_key == '4':
        wrong_input=0
        phone_create()
    elif user_key == '5':
        wrong_input=0
        phone_find()
    elif user_key == '6':
        wrong_input=0
        phone_change()
    elif user_key == '7':
        wrong_input=0
        phone_delete()
    elif user_key == '8':
        phone_out()
        break
    else:
        print('Ввод некорректный')
        wrong_input +=1
print('Работа программы завершена')