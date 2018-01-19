from app.meda_sync_search.services.loader import Loader
from app.meda_sync_search.transformers.equipments_data_transformer import EquipmentsDataTransformer


class EquipmentLoader(Loader):

    @property
    def list(self):
        if not EquipmentLoader._list:
            equipments_data_transformer = EquipmentsDataTransformer(self.data)
            equipments = equipments_data_transformer.transform()
            EquipmentLoader._list = equipments

        return EquipmentLoader._list
