import os
import random
import json
import pandas as pd
import csv
import openpyxl


def data_encoding(data: bytes) -> None:

    decode_data_str = data.decode('utf-8')
    encode_data_latin = decode_data_str.encode('latin1')
    latin_decote_str = encode_data_latin.decode('latin1')

    print(
        f"\nFirst byte data - {data} \
        \nDecode byte data to utf-8 - {decode_data_str} \
        \nEncode str data to Latin1 - {encode_data_latin} \
        \nDecode byte data to str - {latin_decote_str}")


def file_handling_txt(cwd: str, data_folder: str) -> None:

    with open(f'{cwd}/{data_folder}/result.txt', 'w+') as f:

        input_value_1 = input('Input string data #1: ')
        input_value_2 = input('Input string data #2: ')

        for string in [input_value_1, input_value_2]:
            f.write(f'{string}\n')

    with open(f'{cwd}/{data_folder}/file_1.txt', 'a+') as f:
        input_value_3 = input('Input string data #3: ')
        input_value_4 = input('Input string data #4: ')

        for string in [input_value_3, input_value_4]:
            f.write(f'{string}\n')


def create_json(cwd: str, data_folder: str) -> None:
    data = {}

    for el in range(6):
        random_id = ''.join([random.randint(0, 9) for i in range(6)])

        print(f'Dict value #{el}')
        name = input('Input name: ')
        age = int(input('Input age: '))
        print('\n')

        data[random_id] = (name, age)

    with open(f'{cwd}/{data_folder}/result.json', 'w+') as f:
        json.dump(data, f)


def json_to_csv(cwd: str, data_folder: str) -> None:

    with open(f'{cwd}/{data_folder}/result.json') as f:
        data = json.load(f)

    # Создание DataFrame и транспонирование матрицы
    df = pd.DataFrame(data, index=None).T.reset_index()
    # Добавил столбец с названием строк (Person_#)
    df.insert(0, '', [f'Persone_{i}' for i in range(len(data))])
    # Указал созданный столбец как интексы строк
    df.set_index('', inplace=True)
    df.columns = ["id", "name", "age"]  # Указал название столбцам
    df['phone'] = [
        '097-32-88', '091-22-21', '092-20-45',
        '099-66-12', '029-61-14', '029-71-25'
    ]  # Создал столбец с телефонами

    df = df.T  # Транспонирование матрицы

    df.to_csv(f'{cwd}/{data_folder}/result.csv', header=True,
              index=True)  # Сохранил DataFrame в файл .csv


def csv_to_xlsx(cwd: str, data_folder: str) -> None:
    wb = openpyxl.Workbook()
    ws = wb.active

    with open(f'{cwd}/{data_folder}/result.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            ws.append(row)

    wb.save(f'{cwd}/{data_folder}/result.xlsx')


if __name__ == "__main__":

    cwd = os.getcwd()
    data_folder = 'data'

    bite_value = b'r\xc3\xa9sum\xc3\xa9'
    data_encoding(bite_value)

    file_handling_txt(cwd, data_folder)
    create_json(cwd, data_folder)
    json_to_csv(cwd, data_folder)
    csv_to_xlsx(cwd, data_folder)
