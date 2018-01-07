from app.prescription_drug_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer

from tests.prescription_drug_search.fixtures import expected_prescriptions_data


def test_prescriptions_data_transformer_init():
    prescriptions_data = expected_prescriptions_data
    prescriptions_data_transformer = PrescriptionsDataTransformer(prescriptions_data)

    assert prescriptions_data_transformer
    assert expected_prescriptions_data == prescriptions_data_transformer.prescriptions_data
