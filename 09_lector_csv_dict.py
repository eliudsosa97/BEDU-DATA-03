import csv

FILE_NAME = 'employees.csv'

with open(FILE_NAME) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        hired_date = row.get('Hire Date')
        name = row.get('Name')
        print(f'{name} was hired on {hired_date}')