import csv


class FileService:
    def __init__(self):
        pass

    @staticmethod
    def write_data_into_csv(file_name, data):
        with open(file_name, 'w') as f_output:
            csv_output = csv.writer(f_output)

            csv_output.writerows(data)
