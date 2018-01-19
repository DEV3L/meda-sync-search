from collections import OrderedDict
from unittest.mock import patch

from app.meda_sync_search.models.prescription import Prescription
from app.meda_sync_search.services.prescription_loader import PrescriptionLoader

expected_prescriptions_data = [
    OrderedDict(
        [('NDC Description', '12-HR DECONGEST 120 MG CAPLET'), ('NDC', '113005452'), ('NADAC_Per_Unit', ' $0.34 '),
         ('Effective_Date', '5/17/17'), ('Pricing_Unit', 'EA'), ('OTC', 'Y'), ('Brand/Generic', 'G'),
         ('As of Date', '6/7/17'), ('High Cost', 'Low')]),
]

expected_prescription = Prescription(
    description='12-HR DECONGEST 120 MG CAPLET',
    national_drug_code=113005452,
    cost_per_unit=0.34,
    pricing_unit='EA',
    is_over_the_counter=True,
    is_brand=False,
    is_high_cost=False
)

def test_init_prescription_loader_service():
    expected_data_file_path = '/'
    prescription_loader = PrescriptionLoader(expected_data_file_path)

    assert prescription_loader
    assert expected_data_file_path == prescription_loader.data_file_path


@patch('app.meda_sync_search.services.prescription_loader.PrescriptionLoader._read')
def test_prescriptions_data_property(mock_read):
    expected_mock_read_call_count = 1
    mock_read.return_value = expected_prescriptions_data

    prescription_loader = PrescriptionLoader('')

    assert expected_prescriptions_data == prescription_loader.data
    assert expected_prescriptions_data == prescription_loader.data
    assert expected_mock_read_call_count == mock_read.call_count


def test_prescriptions():
    PrescriptionLoader._list = None
    expected_prescriptions_list = [expected_prescription]

    prescription_loader = PrescriptionLoader('')
    prescription_loader.prescriptions_data = expected_prescriptions_data

    prescriptions_list = prescription_loader.list

    assert expected_prescriptions_list == prescriptions_list


@patch('app.meda_sync_search.services.prescription_loader.PrescriptionsDataTransformer')
def test_prescriptions_cache(mock_prescriptions_data_transformer):
    PrescriptionLoader._list = None
    expected_call_count = 1

    prescription_loader = PrescriptionLoader('')
    _ = prescription_loader.list
    _ = prescription_loader.list

    assert expected_call_count == mock_prescriptions_data_transformer.call_count
