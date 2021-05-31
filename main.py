import csv
import os
import sys

with open(sys.argv[1], mode='r') as input_file:
    csv_reader = csv.reader(input_file)
    for line in csv_reader:
        for item in line:
            print(item + ',', end='')
        print()

def evaluate(item, index=None):
    return item