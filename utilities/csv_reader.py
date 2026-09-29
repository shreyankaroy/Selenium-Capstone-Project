import csv


class CSVReader:

    @staticmethod
    def read_data(file_path):

        with open(file_path, mode="r", newline="") as file:

            reader = csv.DictReader(file)

            return list(reader)