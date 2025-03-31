import csv

# with open("/home/timofey/Dev/catalog (1).csv", "r", encoding="utf-8") as file:
with open("file_output.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file, delimiter=';')

    for row in csv_reader:
        print(row)
