import csv

def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    new_contact = [surname, name, phone]
    with open('phonebook.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(new_contact)
