from csv import DictReader

from app.meda_sync_search.transformers.equipments_data_transformer import EquipmentsDataTransformer


class EquipmentLoader:
    _equipments_data = None
    _list = None

    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    @property
    def equipments(self):
        if not EquipmentLoader._list:
            equipments_data_transformer = EquipmentsDataTransformer(self.equipments_data)
            equipments = equipments_data_transformer.transform()
            EquipmentLoader._list = equipments

        return EquipmentLoader._list

    @property
    def equipments_data(self):
        if not self._equipments_data:
            EquipmentLoader._equipments_data = self._read()

        return self._equipments_data

    @equipments_data.setter
    def equipments_data(self, equipments_data):
        self._equipments_data = equipments_data

    def _read(self):
        with open(self.data_file_path, 'r') as csvfile:
            equipments_data = DictReader(csvfile)
            return [equipment_data for equipment_data in equipments_data]
