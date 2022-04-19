import matplotlib.pyplot as plt
import numpy as np

from CsvReader import CsvReader


class CardWithdrawQuery:
    def __init__(self, csv_file):
        self.reader = CsvReader(csv_file)

    # function to retrieve the average card withdrawals for XYZ cards and Other cards
    def get_means(self):
        xyz_data = []
        other_data = []
        for row in self.reader.read():
            data1 = int(row[3])
            xyz_data.append(data1)
            data2 = int(row[4])
            other_data.append(data2)

        xyz_mean = round(sum(xyz_data) / len(xyz_data))
        other_mean = round(sum(other_data) / len(other_data))

        return xyz_mean, other_mean

    def run(self):
        fig, ax = plt.subplots()

        data = self.get_means()[0]  # average amout of xyz card withdrawals
        data2 = self.get_means()[1]  # average amout of other card withdrawals

        labels = ["Average number of card withdrawals per day"]  # x axis label
        xyz_means = data
        other_means = data2

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        xyz_bar = ax.bar(
            x - width / 1, xyz_means, width, label="No Of XYZ Card Withdrawals"
        )
        other_bar = ax.bar(
            x + width / 1, other_means, width, label="No Of Other Card Withdrawals"
        )

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel("scores")
        ax.set_title("Number of card withdrawals comparison")
        ax.set_xticks(x, labels)
        ax.legend()
        ax.bar_label(xyz_bar, padding=3)
        ax.bar_label(other_bar, padding=3)

        fig.tight_layout()

        plt.show()

        # plt.savefig(
        #     "card_withdrawals-bar_chart.png", bbox_inches="tight"
        # )  # first arguement is the name of the file that I want to create and have my graph saved in. Second arguement is used to trim extra whitespaces from the plot
