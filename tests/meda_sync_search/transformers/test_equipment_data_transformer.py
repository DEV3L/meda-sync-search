from collections import OrderedDict

from pytest import mark

from app.meda_sync_search.models.equipment import Equipment
from app.meda_sync_search.transformers.equipment_data_transformer import EquipmentDataTransformer


def test_equipment_transformer_init():
    expected_equipment_data = equipment_data_one
    equipment_data_transformer = EquipmentDataTransformer(expected_equipment_data)

    assert equipment_data_transformer
    assert expected_equipment_data == equipment_data_transformer.data


equipment_data_one = OrderedDict(
    [('HCPCS', 'hcpcs'), ('Description', 'description'), ('Category', 'category'),
     ('Average Cost', ' $0.43 '), ('Modifier', 'modifier')])

expected_equipment_one = Equipment(
    description='description',
    hcpcs='hcpcs',
    average_cost=.43,
    category='category',
    modifier='modifier'
)

equipment_data_two = OrderedDict(
    [('HCPCS', 'hcpcs2'),
     ('Description', 'description2'),
     ('Category', 'category2'),
     ('Average Cost', ' $1.43 '),
     ('Modifier', 'modifier2')])

expected_equipment_two = Equipment(
    description='description2',
    hcpcs='hcpcs2',
    average_cost=1.43,
    category='category2',
    modifier='modifier2'
)


@mark.parametrize("equipment_data, expected_equipment",
                  [
                      (equipment_data_one, expected_equipment_one),
                      (equipment_data_two, expected_equipment_two),
                  ])
def test_transform(equipment_data, expected_equipment):
    equipment_data_transformer = EquipmentDataTransformer(equipment_data)
    assert expected_equipment == equipment_data_transformer.transform()
