from collections import OrderedDict
from unittest.mock import patch

from app.meda_sync_search.models.equipment import Equipment
from app.meda_sync_search.services.loader import Loader

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


def test_init_loader_service():
    expected_data_file_path = '/'

    loader = Loader(expected_data_file_path)

    assert expected_data_file_path == loader.data_file_path


@patch('app.meda_sync_search.services.loader.DictReader')
@patch('builtins.open')
def test_read(mock_open, mock_dict_reader):
    mock_open_context = mock_open.return_value.__enter__.return_value
    mock_dict_reader.return_value = expected_equipments_data

    loader = Loader('')

    equipments_data = loader._read()

    mock_dict_reader.assert_called_with(mock_open_context)
    assert expected_equipments_data == equipments_data


def test_data_setter():
    loader = Loader('')
    loader.data = 'test'

    assert 'test' == loader._data
