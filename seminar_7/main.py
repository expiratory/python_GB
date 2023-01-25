import function as fn


def menu():
    choise = int(input('Введите номер действия:\n'
                       + '1 - Вывод автобуса \n'
                       + '2 - Добавление автобуса \n'
                       + '3 - Вывод водителей \n'
                       + '4 - Добавление водителей \n'
                       + '5 - Вывод маршрута \n'
                       + '6 - Детализированный вывод маршрута \n'
                       + '7 - Добавление маршрута \n'
                       + '8 - Выход \n'))
    if choise == 1:
        fn.print_bus()
    elif choise == 2:
        fn.add_bus()
    elif choise == 3:
        fn.print_driver()
    elif choise == 4:
        fn.add_driver()
    elif choise == 5:
        fn.print_route()
    elif choise == 6:
        fn.detailed_route()
    elif choise == 7:
        fn.add_route()
    elif choise == 8:
        input('Нажмите любую кнопку, чтобы выйти: ')
    else:
        print('Некорректный ввод')


menu()
