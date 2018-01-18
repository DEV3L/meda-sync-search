from app.meda_sync_search.models.equipment import Equipment
from app.meda_sync_search.transformers.data_transformer import DataTransformer


class EquipmentDataTransformer(DataTransformer):
    def transform(self):
        description = self._get_value('Description')
        hcpcs = self._get_value('HCPCS')
        category = self._get_value('Category')
        modifier = self._get_value('Modifier')

        average_cost = float(self._get_value('Average Cost').replace('$', '').replace(',', ''))

        return self._build_equipment(description, hcpcs, category, modifier, average_cost)

    def _build_equipment(self, description, hcpcs, category, modifier, average_cost):
        return Equipment(
            description=description,
            hcpcs=hcpcs,
            category=category,
            modifier=modifier,
            average_cost=average_cost
        )
