from collections import OrderedDict

from app.meda_sync_search.models.prescription import Prescription
from app.meda_sync_search.transformers.prescriptions_data_transformer import PrescriptionsDataTransformer


def test_prescriptions_data_transformer_init():
    prescriptions_data_transformer = PrescriptionsDataTransformer(prescriptions_data)

    assert prescriptions_data_transformer
    assert prescriptions_data == prescriptions_data_transformer.prescriptions_data


def test_transform():
    prescriptions_data_transformer = PrescriptionsDataTransformer(prescriptions_data)

    assert expected_prescriptions == prescriptions_data_transformer.transform()


prescriptions_data = [
    OrderedDict(
        [('NDC Description', 'desc1'), ('NDC', '1'), ('NADAC_Per_Unit', ' $0.34 '),
         ('Effective_Date', '5/17/17'), ('Pricing_Unit', 'EA'), ('OTC', 'Y'), ('Brand/Generic', 'G'),
         ('As of Date', '6/7/17'), ('High Cost', 'Low')]),
    OrderedDict(
        [('NDC Description', 'desc2'), ('NDC', '2'), ('NADAC_Per_Unit', '$1.34'),
         ('Effective_Date', '5/17/17'), ('Pricing_Unit', 'ML'), ('OTC', 'N'), ('Brand/Generic', 'B'),
         ('As of Date', '6/7/17'), ('High Cost', 'High')]),
]

expected_prescriptions = [
    Prescription(
        description='desc1',
        national_drug_code=1,
        cost_per_unit=.34,
        pricing_unit='EA',
        is_over_the_counter=True,
        is_brand=False,
        is_high_cost=False
    ),
    Prescription(
        description='desc2',
        national_drug_code=2,
        cost_per_unit=1.34,
        pricing_unit='ML',
        is_over_the_counter=False,
        is_brand=True,
        is_high_cost=True
    )
]
