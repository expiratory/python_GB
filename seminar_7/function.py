def print_bus():
    with open('bus.txt', 'r', encoding='utf8') as bus:
        for item in bus:
            print(item)


def add_bus():
    with open('bus.txt', 'a+', encoding='utf8') as bus:
        bus.write(input('Введите id автобуса: ') + ',')
        bus.write(input('Введите госномер автобуса: ') + ',' + '\n')
    print_bus()


def print_driver():
    with open('driver.txt', 'r', encoding='utf8') as driver:
        for item in driver:
            print(item)


def add_driver():
    with open('driver.txt', 'a+', encoding='utf8') as driver:
        driver.write(input('Введите id водителя: ') + ',')
        driver.write(input('Введите фамилию водителя: ') + ',' + '\n')
    print_driver()


def print_route():
    with open('marshrut.txt', 'r', encoding='utf8') as marshrut:
        for item in marshrut:
            print(item)


def detailed_route():
    print_route()
    n = int(input(
        'Введите номер строки маршрута, по которому хотите получить детализацию: '))
    n -= 1
    with open('marshrut.txt', 'r', encoding='utf8') as marshrut:
        all_marshrut_list = marshrut.readlines()
        one_line = all_marshrut_list[n].split(',')
        res_line = [one_line[0], one_line[1]]
        bus_id = one_line[2]
        driver_id = one_line[3]
    with open('bus.txt', 'r', encoding='utf8') as bus:
        bus_lines = bus.readlines()
        for item in bus_lines:
            list = item.split(',')
            count = 0
            while count < len(list):
                if list[count] == bus_id:
                    res_line.append(list[count+1])
                count += 1
    with open('driver.txt', 'r', encoding='utf8') as driver:
        driver_lines = driver.readlines()
        for item in driver_lines:
            list = item.split(',')
            count = 0
            while count < len(list):
                if list[count] == driver_id:
                    res_line.append(list[count+1])
                count += 1
    result = (','.join(res_line))
    print(result)


def add_route():
    with open('marshrut.txt', 'a+', encoding='utf8') as marshrut:
        marshrut.write(input('Введите id маршрута: ') + ',')
        marshrut.write(input('Введите номер маршрута: ') + ',')
        marshrut.write(input('Введите id автобуса: ') + ',')
        marshrut.write(input('Введите id водителя: ') + ',' + '\n')
    print_route()
