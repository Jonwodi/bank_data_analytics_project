import csv


class CsvReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self, header=True):
        rows = []
        with open(self.filename) as f:
            reader = csv.reader(f)
            if header:
                next(reader)
            for row in reader:
                rows.append(row)
        return rows
