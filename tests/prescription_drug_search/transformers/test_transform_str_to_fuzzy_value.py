from pytest import mark

from app.prescription_drug_search.transformers.str_transformer import StrTransformer


def test_str_transformer_init():
    expected_str = ''
    str_transformer = StrTransformer(expected_str)

    assert str_transformer
    assert expected_str == str_transformer._str


names = [
    'Catherine', 'Katherine', 'Katarina', 'Johnathan',
    'Jonathan', 'John', 'Teresa', 'Theresa',
    'Smith', 'Smyth', 'Jessica', 'Joshua',
]

fuzzy_list = [
    'CATARAN', 'CATARAN', 'CATARAN', 'JANATAN',
    'JANATAN', 'JAN', 'TARAS', 'TARAS',
    'SNATH', 'SNATH', 'JASAC', 'JAS'
]


@mark.parametrize("name, expected_fuzzy_value",
                  zip(names, fuzzy_list))
def test_fuzzy_property(name, expected_fuzzy_value):
    assert StrTransformer(name).fuzzy == expected_fuzzy_value
