

menu = [          # переменная для с пунктами основного меню
    'открыть файл',
    'сохранить файл',
    'показать все контакты',
    'создать контакт',
    'найти контакт',
    'изменить контакт',
    'удалить контакт',
    'выход'
]

global_phone_book = {}  # глобальная переменная, размещает справочник на время работы с ним


def next_id(phone_book):
    """
    Функция следующего свободного id в справочнике
    """

    if phone_book:
        return max(phone_book) + 1
    return 1


def pause():
    """
     Функция паузы для удобства чтения вывода данных
     """
    input('Нажмите "ввод" для выхода в основное меню')


def phone_open():
    """
     Функция открытия файла и запись данных в глобальную переменную global_phone_book
     """
    with open('phone_book.txt', 'r', encoding='UTF-8') as file:
        data = sorted(file.readlines(), key=lambda x: x[0])
        data = list(map(lambda x: x.strip().split(';'), data))
        for contact in data:
            global_phone_book[next_id(global_phone_book)] = {'name': contact[0], 'phone': contact[1],
                                                             'comment': contact[2]}
        if global_phone_book:
            print('Телефонная книга успешно открыта')
        else:
            print('Телефонная книга пуста')
        return global_phone_book


def phone_show(phone_book, stop=True):
    """
     Функция печати справочника либо отдельный контактов
     """
    if phone_book:
        print('=' * 66)
        for u_id, contact in phone_book.items():
            print(f'{u_id: >2}. {contact['name']: <20} {contact['phone']: <20} {contact['comment']: <20}')
        print('=' * 66)
        if stop:
            pause()

    else:
        print('Телефонная книга не открыта, выберите пункт "открыть файл"')


def phone_create():
    """
     Функция создания контакта и добавления его в global_phone_book
     """
    if global_phone_book:
        contact = {}    # переменная для временного хранения создаваемого контакта
        fields = {'name': 'Введите имя: ', 'phone': 'Введите телефон: ', 'comment': 'Введите комментарий: '}
        for key, field in fields.items():
            contact[key] = input(field)
        u_id = next_id(global_phone_book)
        global_phone_book[u_id] = contact
        print('Успешно создан новый контакт:')
        print(f'{u_id: >2}. {contact['name']: <20} {contact['phone']: <20} {contact['comment']: <20} ')
        print('не забудьте сохранить файл перед выходом')
        pause()
    else:
        print('Телефонная книга не открыта, выберите пункт "открыть файл"')
        pause()


def phone_save():
    """
     Функция записи глобальной переменной global_phone_book в файл
     """
    data = []
    for contact in global_phone_book.values():
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open('phone_book.txt', 'w', encoding='UTF-8') as file:
        file.write(data)
    print('Контакт успешно сохранен')


def phone_find():
    """
     Функция поиска во всех полях global_phone_book по ключевому слову
     """
    result = {}
    key_word = input('Введите слово для поиска: ')
    for u_id, contact in global_phone_book.items():
        for key, field in contact.items():
            if key == 'phone':
                res = []
                for i in field:
                    if i.isdigit():
                        res.append(i)
                field = ''.join(res)
            if key_word.lower() in field.lower():
                result[u_id] = contact
                break
    if result:
        phone_show(result)
    else:
        print('Контакт не найден')
        pause()


def phone_change():
    """
     Функция изменения контакта с выбором поля для изменения
     """
    menu_change = {'Имя': 'name', 'Телефон': 'phone', 'Комментарий': 'comment', 'Выход': None} # переменная меню
    contact_change = {}                     # переменная для временного хранения и изменения выбранного контакта
    user_id_choice = input('Введите порядковый номер контакта который хотите изменить: ')
    if user_id_choice.isdigit() and 0 < int(user_id_choice) < next_id(global_phone_book):
        contact_change[int(user_id_choice)] = global_phone_book[int(user_id_choice)]
        phone_show(contact_change, False)
        while True:
            for i, item in enumerate(menu_change, 1):
                print(f'\t {i}. {item}')
            field_id: str = input("Введите номер поля которое хотите изменить: ")
            if field_id.isdigit() and 0 < int(field_id) < 4:
                global_phone_book[int(user_id_choice)][list(menu_change.values())[int(field_id) - 1]] = input(
                    f'Введите {list(menu_change.keys())[int(field_id) - 1]}: ')
                contact_change[int(user_id_choice)] = global_phone_book[int(user_id_choice)]
                phone_show(contact_change, False)
            elif int(field_id) == 4:
                break
            else:
                print("Введён неверный символ")
                pause()
    elif user_id_choice.isdigit():
        print(f'Контакта с порядковым номером {user_id_choice} не существует')
        pause()
    else:
        print("Введён неверный символ")
        pause()


def phone_delete():
    """
      Функция удаления контакта
      """
    contact_del = {}  # переменная вывода выбранного контакта для дополнительного запрос на удаление
    del_id = input('Введите порядковый номер контакта который хотите удалить: ')
    if del_id.isdigit() and 0 < int(del_id) < next_id(global_phone_book):
        contact_del[int(del_id)] = global_phone_book[int(del_id)]
        print('Вы действительно хотите удалить контакт: ')
        phone_show(contact_del, False)
        con_del_id= input('Если да введите "Y": ')
        if con_del_id == 'Y' or con_del_id == 'y':
            print('Контакта удалён')
            del global_phone_book[int(del_id)]
            pause()
    elif del_id.isdigit() and not 0 < int(del_id) < next_id(global_phone_book):
        print(f'Контакта с порядковым номером {del_id} не существует')
        pause()
    else:
        print('Введён не верный символ')
        pause()

def phone_out():
    """
      Функция выхода из программы
      """
    key = input('Введите "Y" что бы сохранить файл: ')
    if key=='Y' or key=='y' and global_phone_book:
        phone_save()
    else:
        print("Телефонная книга пуста или не отрывалась")
        print("сохранение не выполнено")


while True: # цикл с основным меню
    print('Основное меню')
    for i, item in enumerate(menu, 1):
        print(f'\t {i}. {item}')
    user_key = input('Введите номер пункта меню (1-8): ')
    if user_key == '1':
        phone_open()
    elif user_key == '2':
        phone_save()
    elif user_key == '3':
        phone_show(global_phone_book)
    elif user_key == '4':
        phone_create()
    elif user_key == '5':
        phone_find()
    elif user_key == '6':
        phone_change()
    elif user_key == '7':
        phone_delete()
    elif user_key == '8':
        phone_out()
        break
    else:
        print('Ввод некорректный')