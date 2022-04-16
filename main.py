import csv

import matplotlib.pyplot as plt
import numpy as np

filename = "./AggregatedData.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # csv file headers
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # ATM BANK NAME USED THE MOST
    atm_names = []
    for row in reader:
        atm = row[0]
        atm_names.append(atm)
    # print(atm_names)

    # for loop that calculates the frequency of how often each bank atm is used
    frequencies = {}
    for atm in atm_names:
        if atm in frequencies:
            frequencies[atm] += 1
        else:
            frequencies[atm] = 1

print(frequencies)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

for atm, frequency in frequencies.items():
    print(atm)
    print(frequency)

data = [(item.split()) for item in frequencies]
print(data)
