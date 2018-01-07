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
