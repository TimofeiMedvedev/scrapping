import csv
from p_P import array


def writer(parametr):
    with open('file_output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file,  delimiter=';')

        for item in parametr():
            writer.writerow(item)


writer(array)