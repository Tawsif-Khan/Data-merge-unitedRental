import csv
import json
import re
import ast
from turtle import update
header = []


def read_file(path):
    rows = []
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)

        csv_file.close()
    return rows


def update_header(data):
    if data not in header:
        header.append(data)


def extract_dict(data):
    # print(data)
    for cell in data.keys():
        update_header(cell)


main_file = read_file('new.csv')
table_file = read_file('testData.csv')

i = 0
data = {}
results = []

for main_row in main_file:
    if i > 0:
        j = 0
        for col, head in zip(main_row, header):
            if col:
                data[head] = col
                data = dict(data.items())
        for table_row in table_file:
            if j > 0:
                if len(table_row) and len(main_row):

                    if table_row[1] == main_row[4]:
                        attr = ast.literal_eval(table_row[4])
                        extract_dict(attr)
                        data.update(attr)

            j += 1

        results.append(data)
    else:
        header = main_row
    i += 1

with open('unitedRentalAll.csv', mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()

    for res in results:
        writer.writerow(res)
# print(header)
