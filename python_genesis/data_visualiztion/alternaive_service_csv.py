import csv
import os
from posixpath import join

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'alternative_service.csv')) as inputFile:
    csv_reader = csv.reader(inputFile, delimiter = ',')
    line_count = 0

    for row in inputFile:
        if line_count == 0:
            print(f'Column names are {row}')
            line_count = line_count + 1
        else:
            print(row)
            line_count = line_count + 1