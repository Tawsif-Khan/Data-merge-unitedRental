import csv
from genericpath import exists
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
main_data_file = read_file('mainData.csv')
main_table_data_file = read_file('mainTableData.csv')


i = 0
data = {}
results = []

for main_row in main_data_file:
    flag = False
    found = False
    if i > 0:
        j = 0
        for col, head in zip(main_row, header):
            if col:
                data[head] = col
                data = dict(data.items())
                found = True
        for table_row in table_file:
            if j > 0:

                if len(table_row) and len(main_row):

                    if table_row[1] and table_row[4] and (table_row[1] == main_row[4]):
                        attr = ast.literal_eval(table_row[4])
                        attri = {}
                        for key, value in attr.items():
                            attri['attribute:'+key] = value
                        extract_dict(attri)
                        data.update(attri)
                        flag = True
                        break

            j += 1
        j = 0
        if flag == False:
            for table_row in main_table_data_file:
                if j > 0:
                    if len(table_row) and len(main_row):
                        # found = True
                        if table_row[0] and table_row[3] and (table_row[0] == main_row[3]):
                            # print(i)
                            if table_row[4]:
                                attr = ast.literal_eval(table_row[4])
                                attri = {}
                                for key, value in attr.items():
                                    attri['attribute:'+key] = value
                                extract_dict(attri)
                                data.update(attri)

                                break

                j += 1
        if found:
            if 'ID' in data:
                results.append(data)
    else:
        header = main_row
    i += 1

print(len(results))

with open('unitedRentalAllV1.csv', mode='w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()

    for res in results:
        writer.writerow(res)
# print(header)
