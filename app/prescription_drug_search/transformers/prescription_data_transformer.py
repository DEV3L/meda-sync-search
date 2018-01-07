from app.prescription_drug_search.models.prescription import Prescription


class PrescriptionDataTransformer:
    def __init__(self, prescription_data):
        self.prescription_data = prescription_data

    def transform(self):
        description = self._get_value('NDC Description')
        national_drug_code = int(self._get_value('NDC'))
        cost_per_unit = float(self._get_value('NADAC_Per_Unit').replace('$', ''))
        pricing_unit = self._get_value('Pricing_Unit')
        is_over_the_counter = 'Y' == self._get_value('OTC')
        is_brand = 'G' != self._get_value('Brand/Generic')
        is_high_cost = 'High' == self._get_value('High Cost')

        return self._build_prescription(description, national_drug_code, cost_per_unit, pricing_unit,
                                        is_over_the_counter, is_brand, is_high_cost)

    def _get_value(self, key):
        return self.prescription_data[key].strip()

    def _build_prescription(self, description, national_drug_code, cost_per_unit, pricing_unit,
                            is_over_the_counter, is_brand, is_high_cost):
        return Prescription(
            description=description,
            national_drug_code=national_drug_code,
            cost_per_unit=cost_per_unit,
            pricing_unit=pricing_unit,
            is_over_the_counter=is_over_the_counter,
            is_brand=is_brand,
            is_high_cost=is_high_cost
        )
