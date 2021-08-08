import csv


FILE_PATH = "data/data.csv"
STORAGE = {}

def write(data):
    with open(FILE_PATH, 'a+') as file:
        writer = csv.DictReader(file, fieldnames=["id", "citi"], quoting=csv.QUOTE_ALL)
        writer.writerow(data)

