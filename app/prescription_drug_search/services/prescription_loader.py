from csv import DictReader


class PrescriptionLoader:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self._prescriptions_data = None

    @property
    def prescriptions_data(self):
        if not self._prescriptions_data:
            self._prescriptions_data = self._read()

        return self._prescriptions_data

    def _read(self):
        with open(self.data_file_path, 'r') as csvfile:
            prescriptions_data = DictReader(csvfile)
            return [prescription_data for prescription_data in prescriptions_data]
