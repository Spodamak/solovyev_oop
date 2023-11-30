from tabulate import tabulate

class AutoCatalog:

    def __init__(self, file_name = r'C:\Users\chete\Desktop\ооп\auto.txt'):
        self.file_name = file_name

    def _read_catalog(self):
        with open(self.file_name, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
        return [line.strip().split(',') for line in lines]

    def _get_valid_input(self):
        while True:
            user_input = input()
            if user_input.isdigit() or user_input.isalpha():
                return user_input
            else:
                print('Введено неверно!')

    def _check_if_number_in(self, str_number):
        lines = self._read_catalog()
        if int(str_number) > (len(str_number)-1):
            print('Ошибка: Такой номер отсутствует!')
            return None
        return self._get_car_by_number(str_number, lines)

    def _get_car_by_number(self, str_number, lines):
        # res = self._get_header_row(lines)
        res = []
        res.append(self._get_header_row(lines))
        num = int(str_number)
        row = lines[num]
        res.append(row)
        return res

    def show_all(self):
        catalog = self._read_catalog()
        table = tabulate(catalog, headers="firstrow", tablefmt="fancy_grid", stralign='center')
        print(table)

    def _get_header_row(self, lines):
        # parameters = str(lines[0])
        # return parameters.strip().split(',')
        return lines[0]

    def add_car(self):
        lines = self._read_catalog()
        row = self._get_header_row(lines)
        new_line = self._get_new_car_row(lines, row)
        lines.append(new_line)
        self._write_catalog(lines)

    def search_car(self):
        print('"Ф" - Поиск по фирме машины')
        print('"М" - Поиск по моделе машины')
        print('"Н" - Поиск по номеру на машине')
        print('"Ц" - Поиск по цвету машины')
        print('"Г" - Поиск по году выпуска')
        search_by = self._get_valid_input()
        lines = self._read_catalog()

        if not lines[1:]:
            print('В базе нет машин!')
            return

        if search_by == 'Ф':
            print('Введите фирму:')
            search_value = input()
            catalog = self._search_by_firm(lines, search_value)
            self._display_search_result(catalog)

        elif search_by == 'М':
            print('Введите модель:')
            search_value = input()
            catalog = self._search_by_model(lines, search_value)
            self._display_search_result(catalog)

        elif search_by == 'Н':
            print('Введите номер:')
            search_value = input()
            catalog = self._search_by_number(lines, search_value)
            self._display_search_result(catalog)

        elif search_by == 'Ц':
            print('Введите цвет:')
            search_value = input()
            catalog = self._search_by_colour(lines, search_value)
            self._display_search_result(catalog)

        elif search_by == 'Г':
            print('Введите год выпуска:')
            search_value = input()
            catalog = self._search_by_year(lines, search_value)
            self._display_search_result(catalog)

        else:
            print('Неподходящее значение!')


    def delete_car(self):
        lines = self._read_catalog()
        print('Введите номер машины в списке:')
        str_number = self._get_valid_input()

        if int(str_number) > (len(lines) - 1):
            print('Ошибка: Такой номер отсутствует!')
            return

        line_to_del = self._find_line_to_delete(lines, str_number)
        del lines[line_to_del]

        self._update_line_numbers(lines)
        # self._write_catalog(lines)

    def update_car(self):
        lines = self._read_catalog()
        print('Введите номер машины в списке:')
        str_number = self._get_valid_input()

        if int(str_number) == 0 or (int(str_number) > (len(lines) - 1)):
            print('Ошибка: Такой номер отсутствует!')
            return

        print('Введите название параметра:')
        res = []
        res.append(self._get_header_row(lines))
        while True:
            name_parameter = input()
            if name_parameter not in res[0]:
                print('Неизвестный параметр!')
            else:
                break

        print('Новая характеристика:')
        new_parameter = input()

        # res.append(self._get_header_row(lines))
        # parameters = lines[0]
        # row = self._get_header_row(lines)

        # if name_parameter not in row:



        number_parameter = res[0].index(name_parameter)
        # ok_line = self._get_car_by_number(str_number, lines)

        # ok_line[number_parameter] = new_parameter

        num = int(str_number)
        lines[num][number_parameter] = new_parameter
        # new_line = ','.join(map(str, [num] + ok_line[1:])) + '\n'

        self._write_catalog(lines)


    def _write_catalog(self, lines):
        with open(self.file_name, 'w', encoding='UTF-8') as file:
            file.writelines(','.join(map(str, line)) + '\n' for line in lines)

    def _get_new_car_row(self, lines, header_row):
        new_row = [str(len(lines))]  # Start with the line number
        for element in header_row[1:]:
            # if element == header_row[-1]:
            #     param = self._get_user_input_for_param(element)
            #     new_row.append(param)
            # else:
            #     param = self._get_user_input_for_param(element)
            #     new_row.append(param + ',')
            param = self._get_user_input_for_param(element)
            new_row.append(param)

        # return ','.join(new_row) + '\n'
        return new_row

    def _get_user_input_for_param(self, element):
        if element[-1] == '?':
            while True:
                print(f'{element} (Да или Нет):')
                # param = input() + '\n'
                param = input()
                # if param == 'Да\n' or param == 'Нет\n':
                if param == 'Да' or param == 'Нет':
                    return param
                else:
                    print('Неподходящее значение!')
        else:
            while True:
                print(f'{element}:')
                param = input()
                if len(param) > 0:
                    return param
                else:
                    print('Неподходящее значение!')

    def _search_by_firm(self, lines, firm):
        catalog = [row for row in lines if row[1] == firm or row[1] == 'Фирма']
        return catalog

    def _search_by_model(self, lines, model):
        catalog = [row for row in lines if row[2] == model or row[2] == 'Модель']
        return catalog

    def _search_by_number(self, lines, number):
        catalog = [row for row in lines if row[3] == number or row[3] == 'Номер']
        return catalog

    def _search_by_colour(self, lines, colour):
        catalog = [row for row in lines if row[4] == colour or row[4] == 'Цвет']
        return catalog

    def _search_by_year(self, lines, year):
        catalog = [row for row in lines if row[5] == year or row[5] == 'Год Выпуска']
        return catalog

    def _display_search_result(self, catalog):
        table = tabulate(catalog, headers="firstrow", tablefmt="fancy_grid", stralign='center')
        print(table)

    def _find_line_to_delete(self, lines, str_number):
        for line in range(1,len(lines)):
            if lines[line][0] == str_number or (lines[line][0] + lines[line][1]) == str_number:
                return line

    def _update_line_numbers(self, lines):
        res = []
        res.append(self._get_header_row(lines))
        for line in range(1, len(lines)):
            lines[line][0] = str(line)
            new_line = lines[line]
            res.append(new_line)
            # row = lines[line]
            # num = line - 1
            # new_line = ','.join(map(str, [num] + row[1:])) + '\n'
            # lines[line] = new_line

        self._write_catalog(res)


if __name__ == "__main__":
    auto_catalog = AutoCatalog()

    while True:
        print('')
        print('        Меню Ввода')
        print('')
        print('  "Все"    - Открыть список машин')
        print('"Добавить" - Добавить машину в список')
        print(' "Поиск"   - Найти машину по параметру')
        print('"Изменить" - Изменить параметр у машины')
        print('"Удалить"  - Удалить машину')
        print('"Закрыть"  - Остановить программу')
        print('')

        command = input()

        if command.lower() == 'все':
            auto_catalog.show_all()

        elif command.lower() == 'добавить':
            auto_catalog.add_car()

        elif command.lower() == 'поиск':
            auto_catalog.search_car()

        elif command.lower() == 'удалить':
            auto_catalog.delete_car()

        elif command.lower() == 'изменить':
            auto_catalog.update_car()

        elif command.lower() == 'закрыть':
            print('\nПрограмма остановлена')
            break

