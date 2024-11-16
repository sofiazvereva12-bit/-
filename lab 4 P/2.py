import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Чтение содержимого CSV файла
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [OrderedDict(row) for row in reader]  # Преобразуем каждую строку в OrderedDict

    # Сериализация в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")