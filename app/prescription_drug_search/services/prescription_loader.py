from csv import DictReader


class PrescriptionLoader:
    _prescriptions_data = None

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path


    @property
    def prescriptions_data(self):
        if not self._prescriptions_data:
            PrescriptionLoader._prescriptions_data = self._read()

        return self._prescriptions_data

    def _read(self):
        with open(self.data_file_path, 'r') as csvfile:
            prescriptions_data = DictReader(csvfile)
            return [prescription_data for prescription_data in prescriptions_data]
