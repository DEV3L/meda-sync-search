from app.prescription_drug_search.transformers.str_transformer import StrTransformer


class Search:
    def __init__(self, value, prescriptions):
        _value = value.lower()
        self.value = _value
        self.fuzzy_value = StrTransformer(self.value).fuzzy

        self.prescriptions = prescriptions
        self._prescriptions = None if value else prescriptions

    @property
    def results(self):
        if self._prescriptions:
            return self._prescriptions

        _prescriptions = self._value_results
        _prescriptions.extend(self._fuzzy_results)
        _prescriptions = list(set(_prescriptions))

        self._prescriptions = _prescriptions
        return self._prescriptions

    @property
    def _value_results(self):
        value_prescriptions = [prescription for prescription in self.prescriptions
                               if (len(self.value) > 1 and self.value in prescription.description.lower()) or
                               (len(self.value) == 1 and prescription.description.lower()[:1] == self.value)]
        return value_prescriptions

    @property
    def _fuzzy_results(self):
        fuzzy_prescriptions = [prescription for prescription in self.prescriptions
                               if prescription.fuzzy.startswith(self.fuzzy_value)]
        return fuzzy_prescriptions
