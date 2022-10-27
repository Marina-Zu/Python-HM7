import csv
 
def read_data():
    with open('phonebook.csv', 'r', encoding="utf-8") as file:  
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))
        file.close()
