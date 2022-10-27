import log

def check_menu(quan):
    while True:
        try:
            ent_menu = input()
            while int(ent_menu) not in range (1, quan):
                print ('\nНеверный ввод! Повторите ввод:')
                log.logger("Неверный пункт меню", data_description = "Ошибка ввода") 
                ent_menu = input()
            return int(ent_menu)
        except ValueError:
            print ('\nНеверный формат! Повторите ввод:')
            log.logger("Неверный формат ввода меню", data_description = "Ошибка ввода")