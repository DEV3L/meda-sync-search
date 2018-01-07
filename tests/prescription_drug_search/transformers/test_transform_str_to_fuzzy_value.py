from app.prescription_drug_search.transformers.str_transformer import StrTransformer


def test_str_transformer_init():
    expected_str = ''
    str_transformer = StrTransformer(expected_str)

    assert str_transformer
    assert expected_str == str_transformer._str
