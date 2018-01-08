import hashlib

from app.prescription_drug_search.models.prescription import Prescription

expected_serialize_str = b'{"description": "", "fuzzy": "", ' \
                         b'"national_drug_code": 0, "cost_per_unit": 0, ' \
                         b'"pricing_unit": "", "is_over_the_counter": false, ' \
                         b'"is_brand": false, "is_high_cost": false}'


def test_init_prescription():
    prescription = Prescription()

    assert prescription


def test_init_prescription_with_keyword_args():
    prescription = Prescription(
        description='apple',
        national_drug_code=0,
        cost_per_unit=0,
        pricing_unit='',
        is_over_the_counter=False,
        is_brand=False,
        is_high_cost=False
    )

    assert prescription
    assert 'APL' == prescription.fuzzy


def test_serialize():
    prescription = Prescription()
    assert expected_serialize_str == prescription.serialize()


def test_repr():
    prescription = Prescription()
    assert expected_serialize_str == prescription.__repr__()


def test_hash():
    expected_hash = int(hashlib.sha1(expected_serialize_str).hexdigest(), 16)
    prescription = Prescription()
    assert expected_hash == prescription.__hash__()
