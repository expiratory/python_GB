# Создать телефонный справочник с возможностью импорта и экспорта в .txt

def write_data():
    with open('phonebook.txt', 'a+') as data:
        data.write(input('Введите фамилию: ') + ',')
        data.write(input('Введите имя: ') + ',')
        data.write(input('Введите отчество: ') + ',')
        data.write(input('Введите номер телефона: ') + ',' + '\n')

def read_data():
    with open('phonebook.txt', 'r') as data:
        print(data.read())

def find_human_by_name_or_number():
    with open('phonebook.txt', 'r') as data:
        find = input('Введите фамилию, имя, отчество или номер телефона: ')
        finded = False
        for item in data:
            array = item.split(',')
            for i in array:
                if i.lower() == find.lower():
                    finded = True  
                    print(item)
                    break
        if finded == False: print('Такого ФИО или номера телефона в справочнике нет')

def delete_item():
    read_data()
    delete = int(input('Введите номер строки, которую хотите удалить: '))
    delete -= 1
    with open('phonebook.txt', 'r') as data:
        lines = data.readlines()
        del lines[delete]
    with open('phonebook.txt', 'w') as data:
        data.writelines(lines)
    read_data()

def change_number():
    read_data()
    number = int(input('Введите номер строки контакта, телефонный номер которого хотите заменить: '))
    number -= 1
    with open('phonebook.txt', 'r') as data:
        lines = data.readlines()
        array = lines[number].split(',')
        array[3] = input('Введите новый номер телефона: ')
        lines[number] = (','.join(array))
    with open('phonebook.txt', 'w') as data:
        data.writelines(lines)
    read_data()

def menu():
    choise = int(input('Введите номер действия: \n'
                        + '1 - Показать все записи \n'
                        + '2 - Найти запись по вхождению частей имени \n'
                        + '3 - Найти запись по телефону \n'
                        + '4 - Добавить новый контакт \n'
                        + '5 - Удалить контакт \n'
                        + '6 - Изменить номер телефона у контакта \n'
                        + '7 - Выход \n'))
    if choise == 1: read_data()
    if choise == 2 or choise == 3: find_human_by_name_or_number()
    if choise == 4: write_data()
    if choise == 5: delete_item()
    if choise == 6: change_number()
    if choise == 7: input('Нажмите любую кнопку, чтобы выйти: ')
    else: print('Некорректный ввод')

menu()