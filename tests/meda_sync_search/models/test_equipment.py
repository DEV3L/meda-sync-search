import hashlib

from app.meda_sync_search.models.equipment import Equipment

expected_serialize_str = b'{' \
                         b'"description": "", ' \
                         b'"fuzzy": "", ' \
                         b'"hcpcs": "", ' \
                         b'"average_cost": 0, ' \
                         b'"category": "", ' \
                         b'"modifier": ""' \
                         b'}'


def test_init_equipment():
    equipment = Equipment()

    assert equipment


def test_init_equipment_with_keyword_args():
    equipment = Equipment(
        description='apple',
        hcpcs='',
        average_cost=0,
        category='',
        modifier='',
    )

    assert equipment
    assert 'APL' == equipment.fuzzy


def test_serialize():
    equipment = Equipment()
    assert expected_serialize_str == equipment.serialize()


def test_hash():
    expected_hash = int(hashlib.sha1(expected_serialize_str).hexdigest(), 16)
    equipment = Equipment()
    assert expected_hash == equipment.__hash__()
