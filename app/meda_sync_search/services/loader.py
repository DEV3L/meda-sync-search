from csv import DictReader


class Loader:
    _data = None
    _list = None

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    @property
    def data(self):
        if not self._data:
            self.__class__._data = self._read()

        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def _read(self):
        with open(self.data_file_path, 'r') as csvfile:
            datas = DictReader(csvfile)
            return [data for data in datas]

