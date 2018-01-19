from app.meda_sync_search.services.loader import Loader
from app.meda_sync_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer


class PrescriptionLoader(Loader):
    @property
    def prescriptions(self):
        if not PrescriptionLoader._list:
            prescriptions_data_transformer = PrescriptionsDataTransformer(self.prescriptions_data)
            prescriptions = prescriptions_data_transformer.transform()
            PrescriptionLoader._list = prescriptions

        return PrescriptionLoader._list


    @property
    def prescriptions_data(self):
        if not self._data:
            PrescriptionLoader._data = self._read()

        return self._data

    @prescriptions_data.setter
    def prescriptions_data(self, prescriptions_data):
        self._data = prescriptions_data
