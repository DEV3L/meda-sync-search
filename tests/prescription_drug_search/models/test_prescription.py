from app.prescription_drug_search.models.prescription import Prescription

def test_init_prescription():
    prescription = Prescription()

    assert prescription


def test_init_prescription_with_keyword_args():
    prescription = Prescription(
        description='',
        national_drug_code=0,
        cost_per_unit=0,
        pricing_unit='',
        is_over_the_counter=False,
        is_brand=False,
        is_high_cost=False
    )

    assert prescription
