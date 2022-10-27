import csv

def search_contact():
    with open('phonebook.csv', 'r', encoding = 'utf-8') as data:
        data2 = data.readlines()
        flag = 1
        name = input('Введите фамилию клиента > \n')
        for line in data2:       
            if name in line:
                flag = 0
                print(line)
        if flag: print('Нет такого имени')
    return name

def del_contact():
     with open('phonebook.csv', 'r', encoding = 'utf-8') as data:
        data2 = data.readlines()
        name = input('Введите фамилию контакта для удаления \n')
        with open('phonebook.csv', 'w', encoding = 'utf-8') as data3:
            for line in data2:       
                if name not in line:
                    data3.write(line)
        return name
