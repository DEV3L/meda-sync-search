import hashlib
import json

from app.prescription_drug_search.transformers.str_transformer import StrTransformer


class Prescription:
    def __init__(self, *,
                 description='',
                 national_drug_code=0,
                 cost_per_unit=0,
                 pricing_unit='',
                 is_over_the_counter=False,
                 is_brand=False,
                 is_high_cost=False):
        self.description = description
        self.fuzzy = StrTransformer(self.description).fuzzy
        self.national_drug_code = national_drug_code
        self.cost_per_unit = cost_per_unit
        self.pricing_unit = pricing_unit
        self.is_over_the_counter = is_over_the_counter
        self.is_brand = is_brand
        self.is_high_cost = is_high_cost

    def serialize(self):
        return self._json

    @property
    def _json(self):
        return json.dumps(self.__dict__).encode()

    def __eq__(self, other):
        is_equal = self.description == other.description \
                   and self.national_drug_code == other.national_drug_code \
                   and self.cost_per_unit == other.cost_per_unit \
                   and self.pricing_unit == other.pricing_unit \
                   and self.is_over_the_counter == other.is_over_the_counter \
                   and self.is_brand == other.is_brand \
                   and self.is_high_cost == other.is_high_cost

        return is_equal

    def __repr__(self):
        return self._json

    def __hash__(self):
        return int(hashlib.sha1(self._json).hexdigest(), 16)
