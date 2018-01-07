from collections import OrderedDict

from pytest import mark

from app.prescription_drug_search.models.prescription import Prescription
from app.prescription_drug_search.transformers.prescription_data_transformer import PrescriptionDataTransformer


def test_prescription_transformer_init():
    expected_prescription_data = prescription_data_one
    prescription_data_transformer = PrescriptionDataTransformer(expected_prescription_data)

    assert prescription_data_transformer
    assert expected_prescription_data == prescription_data_transformer.prescription_data


prescription_data_one = OrderedDict(
    [('NDC Description', 'desc1'), ('NDC', '1'), ('NADAC_Per_Unit', ' $0.34 '),
     ('Effective_Date', '5/17/17'), ('Pricing_Unit', 'EA'), ('OTC', 'Y'), ('Brand/Generic', 'G'),
     ('As of Date', '6/7/17'), ('High Cost', 'Low')])

expected_prescription_one = Prescription(
    description='desc1',
    national_drug_code=1,
    cost_per_unit=.34,
    pricing_unit='EA',
    is_over_the_counter=True,
    is_brand=False,
    is_high_cost=False
)

prescription_data_two = OrderedDict(
    [('NDC Description', 'desc2'), ('NDC', '2'), ('NADAC_Per_Unit', '$1.34'),
     ('Effective_Date', '5/17/17'), ('Pricing_Unit', 'ML'), ('OTC', 'N'), ('Brand/Generic', 'B'),
     ('As of Date', '6/7/17'), ('High Cost', 'High')])

expected_prescription_two = Prescription(
    description='desc2',
    national_drug_code=2,
    cost_per_unit=1.34,
    pricing_unit='ML',
    is_over_the_counter=False,
    is_brand=True,
    is_high_cost=True
)


@mark.parametrize("prescription_data, expected_prescription",
                  [
                      (prescription_data_one, expected_prescription_one),
                      (prescription_data_two, expected_prescription_two),
                  ])
def test_transform(prescription_data, expected_prescription):
    prescription_data_transformer = PrescriptionDataTransformer(prescription_data)
    assert expected_prescription == prescription_data_transformer.transform()
