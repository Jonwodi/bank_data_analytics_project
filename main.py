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

# for loop to extract key and values from frequencies append all keys to a single list and also to v=append values to a seperate list
data_set = []
banks = []
for atm, frequency in frequencies.items():
    atm = atm
    frequency = int(frequency)
    data_set.append(frequency)
    banks.append(atm)


data = data_set  # list of frequency of bank vists
bank_atm = banks  # list of bank atms


def func(pct, allvals):
    absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)


wedges, texts, autotexts = ax.pie(
    data, autopct=lambda pct: func(pct, data), textprops=dict(color="w")
)

ax.legend(
    wedges,
    bank_atm,
    title="Bank ATM",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
)

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("The most used bank ATM")

# plt.show()

plt.savefig(
    "bank-atm_pie-chart.png", bbox_inches="tight"
)  # first arguement is the name of the file that I want to create and have my graph saved in. Second arguement is used to trim extra whitespaces from the plot
