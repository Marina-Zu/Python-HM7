from datetime import datetime as dt

def logger(data, data_description = "действие"):
    time = dt.now().strftime('%m-%Y %H:%M:%S')
    with open('log.csv', 'a', encoding='utf-8') as file:
        file.write('{}; {}; {}\n'
                    .format(time, data_description, data))
                    
def print_log():
    with open('log.csv', 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

