from pytest import mark

from app.meda_sync_search.models.prescription import Prescription
from app.meda_sync_search.services.search import Search


def test_search_init():
    search = Search(None, [])

    assert search
    assert '' == search._value
    assert '' == search.value
    assert '' == search.value_fuzzy

    assert [] == search._items
    assert [] == search.items

    search = Search('Value', [])

    assert search
    assert 'Value' == search._value
    assert 'value' == search.value
    assert 'VAL' == search.value_fuzzy

    assert [] == search._items
    assert None == search.items


def test_value_result_starts_with_when_one_character():
    expected_item = Prescription(description='A')
    expected_items = [expected_item]

    items = []
    items.append(expected_item)
    items.append(Prescription(description='bA'))

    search = Search('a', items)

    assert expected_items == search._value_results


def test_value_result_contains_when_multiple_characters():
    expected_item_first = Prescription(description='ABCD')
    expected_item_second = Prescription(description='BCDE')
    expected_items = [expected_item_first, expected_item_second]

    items = []
    items.append(expected_item_first)
    items.append(expected_item_second)
    items.append(Prescription(description='DEFG'))

    search = Search('bc', items)

    assert expected_items == search._value_results


def test_value_fuzzy_result():
    expected_item_first = Prescription(description='ABECD')
    expected_item_second = Prescription(description='ABICD')
    expected_items = [expected_item_first, expected_item_second]

    items = []
    items.append(expected_item_first)
    items.append(expected_item_second)
    items.append(Prescription(description='DEFG'))

    search = Search('abe', items)

    assert expected_items == search._value_fuzzy_results


def test_value_fuzzy_result_none_fuzzy():
    expected_items = []
    items = [Prescription(description='D')]

    search = Search('D', items)
    search.value_fuzzy = None

    assert expected_items == search._value_fuzzy_results


@mark.parametrize("expected_items, descriptions, search_value",
                  [
                      (['ABECD', 'ABICD'], ['ABECD', 'ABICD', 'DEFG'], 'abe'),
                      (['DEFG'], ['ABECD', 'ABICD', 'DEFG'], 'd'),
                      (['Negative Something', 'Something'],
                       ['Negative Something', 'Something', 'DEFG'], 'neg some')
                  ])
def test_results(expected_items, descriptions, search_value):
    expected_items = [Prescription(description=description) for description in expected_items]
    items = [Prescription(description=description) for description in descriptions]

    search = Search(search_value, items)

    assert expected_items == search.results


def test_results_value_cached():
    expected_items = 'cached value'

    search = Search('test', [])
    search.items = expected_items

    assert expected_items == search.results
