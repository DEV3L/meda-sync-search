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
        self.national_drug_code = national_drug_code
        self.cost_per_unit = cost_per_unit
        self.pricing_unit = pricing_unit
        self.is_over_the_counter = is_over_the_counter
        self.is_brand = is_brand
        self.is_high_cost = is_high_cost

    def __eq__(self, other):
        is_equal = self.description == other.description \
                   and self.national_drug_code == other.national_drug_code \
                   and self.cost_per_unit == other.cost_per_unit \
                   and self.pricing_unit == other.pricing_unit \
                   and self.is_over_the_counter == other.is_over_the_counter \
                   and self.is_brand == other.is_brand \
                   and self.is_high_cost == other.is_high_cost

        return is_equal
