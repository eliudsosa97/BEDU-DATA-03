import csv

FILE_NAME = 'employees.csv'

with open(FILE_NAME) as csv_file:
    # Contexto - Context processor
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)