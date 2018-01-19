from app.meda_sync_search.services.loader import Loader
from app.meda_sync_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer


class PrescriptionLoader(Loader):
    @property
    def list(self):
        if not PrescriptionLoader._list:
            prescriptions_data_transformer = PrescriptionsDataTransformer(self.data)
            prescriptions = prescriptions_data_transformer.transform()
            PrescriptionLoader._list = prescriptions

        return PrescriptionLoader._list

