from csv import DictReader

from app.prescription_drug_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer


class PrescriptionLoader:
    _prescriptions_data = None
    _list = None

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    @property
    def prescriptions(self):
        if not PrescriptionLoader._list:
            prescriptions_data_transformer = PrescriptionsDataTransformer(self.prescriptions_data)
            prescriptions = prescriptions_data_transformer.transform()
            PrescriptionLoader._list = prescriptions

        return PrescriptionLoader._list


    @property
    def prescriptions_data(self):
        if not self._prescriptions_data:
            PrescriptionLoader._prescriptions_data = self._read()

        return self._prescriptions_data

    @prescriptions_data.setter
    def prescriptions_data(self, prescriptions_data):
        self._prescriptions_data = prescriptions_data

    def _read(self):
        with open(self.data_file_path, 'r') as csvfile:
            prescriptions_data = DictReader(csvfile)
            return [prescription_data for prescription_data in prescriptions_data]
