from collections import OrderedDict
from unittest.mock import patch

from app.meda_sync_search.models.equipment import Equipment
from app.meda_sync_search.services.equipment_loader import EquipmentLoader

expected_equipments_data = [
    OrderedDict([('HCPCS', 'hcpcs'), ('Description', 'description'), ('Category', 'category'),
                 ('Average Cost', ' $0.43 '), ('Modifier', 'modifier')])
]

expected_equipment = Equipment(
    description='description',
    hcpcs='hcpcs',
    average_cost=.43,
    category='category',
    modifier='modifier'
)


def test_init_equipment_loader_service():
    expected_data_file_path = '/'
    equipment_loader = EquipmentLoader(expected_data_file_path)

    assert equipment_loader
    assert expected_data_file_path == equipment_loader.data_file_path



@patch('app.meda_sync_search.services.equipment_loader.EquipmentLoader._read')
def test_equipments_data_property(mock_read):
    expected_mock_read_call_count = 1
    mock_read.return_value = expected_equipments_data

    equipment_loader = EquipmentLoader('')

    assert expected_equipments_data == equipment_loader.equipments_data
    assert expected_equipments_data == equipment_loader.equipments_data
    assert expected_mock_read_call_count == mock_read.call_count


def test_equipments():
    EquipmentLoader._list = None
    expected_equipments_list = [expected_equipment]

    equipment_loader = EquipmentLoader('')
    equipment_loader.equipments_data = expected_equipments_data

    equipments_list = equipment_loader.equipments

    assert expected_equipments_list == equipments_list


@patch('app.meda_sync_search.services.equipment_loader.EquipmentsDataTransformer')
def test_equipments_cache(mock_equipments_data_transformer):
    EquipmentLoader._list = None
    expected_call_count = 1

    equipment_loader = EquipmentLoader('')
    _ = equipment_loader.equipments
    _ = equipment_loader.equipments

    assert expected_call_count == mock_equipments_data_transformer.call_count
