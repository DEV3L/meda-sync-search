from unittest.mock import patch

from app.prescription_drug_search.services.prescription_loader import PrescriptionLoader
from tests.prescription_drug_search.fixtures import expected_prescriptions_data


def test_init_prescription_loader_service():
    expected_data_file_path = '/'
    prescription_loader = PrescriptionLoader(expected_data_file_path)

    assert prescription_loader
    assert expected_data_file_path == prescription_loader.data_file_path


@patch('app.prescription_drug_search.services.prescription_loader.DictReader')
@patch('builtins.open')
def test_read(mock_open, mock_dict_reader):
    mock_open_context = mock_open.return_value.__enter__.return_value
    mock_dict_reader.return_value = expected_prescriptions_data

    prescription_loader = PrescriptionLoader('')

    prescriptions_data = prescription_loader._read()

    mock_dict_reader.assert_called_with(mock_open_context)
    assert expected_prescriptions_data == prescriptions_data


@patch('app.prescription_drug_search.services.prescription_loader.PrescriptionLoader._read')
def test_prescriptions_data_property(mock_read):
    expected_mock_read_call_count = 1
    mock_read.return_value = expected_prescriptions_data

    prescription_loader = PrescriptionLoader('')

    assert expected_prescriptions_data == prescription_loader.prescriptions_data
    assert expected_prescriptions_data == prescription_loader.prescriptions_data
    assert expected_mock_read_call_count == mock_read.call_count


