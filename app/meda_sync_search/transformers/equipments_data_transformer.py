from app.meda_sync_search.transformers.equipment_data_transformer import EquipmentDataTransformer


class EquipmentsDataTransformer:
    def __init__(self, equipments_data):
        self.equipments_data = equipments_data

    def transform(self):
        equipments = []

        for equipment_data in self.equipments_data:
            equipment = EquipmentDataTransformer(equipment_data).transform()
            equipments.append(equipment)

        return equipments
