from csv import DictReader


class Loader:
    _data = None
    _list = None

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def _read(self):
        with open(self.data_file_path, 'r') as csvfile:
            datas = DictReader(csvfile)
            return [data for data in datas]
