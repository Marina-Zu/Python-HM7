import check
import record_data
import read_data
import checklist
import log

def menu_1 ():
    print('\nВыберите пункт меню\n \
1 - Просмотр справочника\n 2 - Внесение изменений \n 3 - Выход')
    type_menu_1 = check.check_menu(4)
    if type_menu_1 == 1:
        log.logger("Телефонный справочник", data_description = "Запуск")
        read_data.read_data()
    elif type_menu_1 == 2:
        log.logger("Внесение изменений", data_description = "Запуск")        
        menu_2()


def menu_2 ():
    print('\nЧто будем делать?\n \
1 - Найти контакт\n 2 - Добавить контакт\n 3 - Удалить запись\n 4 - Главное меню\n 5 - Выход')
    type_menu_2 = check.check_menu(6)
    if type_menu_2 == 1:
        log.logger("Поиск контакта", data_description = "Выбор")
        record_data.search_contact()
    elif type_menu_2 == 2:
        log.logger("Добавить контакт", data_description = "Выбор")
        checklist.add_contact()
    elif type_menu_2 == 3:
        log.logger("Удалить контакт", data_description = "Выбор")
        record_data.del_contact()
    elif type_menu_2 == 4:
        log.logger("Главное меню", data_description = "Возврат")
        return menu_1()
    else:
        return end_prog()
    return type_menu_2

    
def end_prog ():
    print('\nДо скорых встреч!')
    log.logger("по команде пользователя", data_description = "Выход") 
    exit()


print(" <Телефонный справочник>")

log.logger("Вход в программу", data_description = "Запуск")
answer = 1
while answer == 1:
    menu_1()
    print('\nХотите выполнить новую операцию?\n\
    1 - Да\n\
    2 - Нет')
    answer = check.check_menu(3)
else:
    end_prog()