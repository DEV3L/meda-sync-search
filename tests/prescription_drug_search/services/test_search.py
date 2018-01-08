from app.prescription_drug_search.models.prescription import Prescription
from app.prescription_drug_search.services.search import Search


def test_search_init():
    search = Search(None, [])

    assert search
    assert '' == search._value
    assert '' == search.value
    assert '' == search.value_fuzzy

    assert [] == search._prescriptions
    assert [] == search.prescriptions

    search = Search('Value', [])

    assert search
    assert 'Value' == search._value
    assert 'value' == search.value
    assert 'VAL' == search.value_fuzzy

    assert [] == search._prescriptions
    assert None == search.prescriptions


def test_value_result_starts_with_when_one_character():
    expected_prescription = Prescription(description='A')
    expected_prescriptions = [expected_prescription]

    prescriptions = []
    prescriptions.append(expected_prescription)
    prescriptions.append(Prescription(description='bA'))

    search = Search('a', prescriptions)

    assert expected_prescriptions == search._value_results


def test_value_result_contains_when_multiple_character():
    expected_prescription_first = Prescription(description='ABCD')
    expected_prescription_second = Prescription(description='BCDE')
    expected_prescriptions = [expected_prescription_first, expected_prescription_second]

    prescriptions = []
    prescriptions.append(expected_prescription_first)
    prescriptions.append(expected_prescription_second)
    prescriptions.append(Prescription(description='DEFG'))

    search = Search('bc', prescriptions)

    assert expected_prescriptions == search._value_results
