from app.meda_sync_search.services.loader import Loader
from app.meda_sync_search.transformers.equipments_data_transformer import EquipmentsDataTransformer


class EquipmentLoader(Loader):

    @property
    def equipments(self):
        if not EquipmentLoader._list:
            equipments_data_transformer = EquipmentsDataTransformer(self.equipments_data)
            equipments = equipments_data_transformer.transform()
            EquipmentLoader._list = equipments

        return EquipmentLoader._list

    @property
    def equipments_data(self):
        if not self._data:
            EquipmentLoader._data = self._read()

        return self._data

    @equipments_data.setter
    def equipments_data(self, equipments_data):
        self._data = equipments_data
