import matplotlib.pyplot as plt
import numpy as np

from CsvReader import CsvReader


class DayFrequencyQuery:
    def __init__(self, csv_file):
        self.reader = CsvReader(csv_file)

    def get_frequencies(self):
        days = [row[8].title() for row in self.reader.read()]

        # for loop that calculates the frequency of bank vists per week day
        frequencies = {}
        for day in days:
            if day in frequencies:
                frequencies[day] += 1
            else:
                frequencies[day] = 1

        return frequencies

    def percentage_vists(self, pct, allvals):
        absolute = int(np.round(pct / 100.0 * np.sum(allvals)))
        return "{:.1f}%\n({:d}\nvists)".format(pct, absolute)

    def run(self):
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        data = list(self.get_frequencies().values())  # list of frequency of bank vists

        wedges, texts, autotexts = ax.pie(
            data,
            autopct=lambda pct: self.percentage_vists(pct, data),
            textprops=dict(color="w"),
        )

        bank_atms = list(self.get_frequencies().keys())  # list of bank atms

        ax.legend(
            wedges,
            bank_atms,
            title="Week Days",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1),
        )

        plt.setp(autotexts, size=6, weight="bold")

        ax.set_title("Frequency of bank ATM transactions per week day")

        plt.show()

        # plt.savefig(
        #     "week_day_pie-chart.png", bbox_inches="tight"
        # )  # first arguement is the name of the file that I want to create and have my graph saved in. Second arguement is used to trim extra whitespaces from the plot
