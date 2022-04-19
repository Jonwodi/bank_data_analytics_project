import matplotlib.pyplot as plt

from CsvReader import CsvReader


class FestivalRelgionQuery:
    def __init__(self, csv_file):
        self.reader = CsvReader(csv_file)

    def get_frequencies(self):
        festivals = [row[9].title() for row in self.reader.read()]

        # for loop that calculates the frequency of bank transcations based on festival relgion
        frequencies = {}
        for festival in festivals:
            if festival in frequencies:
                frequencies[festival] += 1
            else:
                frequencies[festival] = 1

        return frequencies

    def run(self):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = list(self.get_frequencies().keys())  # list of festival religions
        data = list(self.get_frequencies().values())  # list of frequency of bank vists
        explode = (
            0.9,
            0.9,
            0.9,
            0.9,
            0.1,
        )  # to section out a slice of the pie chart from the pie chart

        fig1, ax = plt.subplots()
        ax.pie(
            data,
            explode=explode,
            labels=labels,
            autopct="%1.1f%%",
            shadow=True,
            startangle=180,
        )
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

        ax.set_title("Percentage (%) of bank transactions based on Festival Relgion")

        plt.legend(title="Festival Relgion")

        plt.show()

        # plt.savefig(
        #     "festival-relgion_pie-chart.png", bbox_inches="tight"
        # )  # first arguement is the name of the file that I want to create and have my graph saved in. Second arguement is used to trim extra whitespaces from the plot
