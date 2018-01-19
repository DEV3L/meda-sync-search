from collections import OrderedDict

from app.meda_sync_search.models.equipment import Equipment
from app.meda_sync_search.transformers.equipments_data_transformer import EquipmentsDataTransformer


def test_equipments_data_transformer_init():
    equipments_data_transformer = EquipmentsDataTransformer(equipments_data)

    assert equipments_data_transformer
    assert equipments_data == equipments_data_transformer.equipments_data


def test_transform():
    equipments_data_transformer = EquipmentsDataTransformer(equipments_data)

    assert expected_equipments == equipments_data_transformer.transform()


equipments_data = [
    OrderedDict(
        [('Description', 'description1'),
         ('HCPCS', 'hcpcs1'),
         ('Category', 'category1'),
         ('Average Cost', ' $1 '),
         ('Modifier', 'modifier1')]),
    OrderedDict(
        [('Description', 'description2'),
         ('HCPCS', 'hcpcs2'),
         ('Category', 'category2'),
         ('Average Cost', ' $2 '),
         ('Modifier', 'modifier2')])
]

expected_equipments = [
    Equipment(
        description='description1',
        hcpcs='hcpcs1',
        category='category1',
        modifier='modifier1',
        average_cost=1
    ),
    Equipment(
        description='description2',
        hcpcs='hcpcs2',
        category='category2',
        modifier='modifier2',
        average_cost=2
    )
]
