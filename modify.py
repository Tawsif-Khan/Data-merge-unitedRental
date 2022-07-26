import csv
from genericpath import exists
import json
import re
import ast
from turtle import update


def read_file(path):
    rows = []
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            rows.append(row)

        csv_file.close()
    return rows


data = read_file('unitedRentalAllV1.csv')

for row in data:
    print(row)
