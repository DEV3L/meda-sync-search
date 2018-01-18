from app.meda_sync_search.transformers.str_transformer import StrTransformer


class Search:
    def __init__(self, value, prescriptions):
        self._value = value or ''
        self.value = self._value.lower()
        self.value_fuzzy = StrTransformer(self._value).fuzzy

        self._prescriptions = prescriptions if prescriptions != None else []
        self.prescriptions = None if value else prescriptions

    @property
    def results(self):
        if self.prescriptions:
            return self.prescriptions

        _prescriptions = self._value_results
        _prescriptions.extend(self._value_fuzzy_results)
        _prescriptions = list(set(_prescriptions))
        _prescriptions.sort(key=lambda prescription: prescription.description)

        self.prescriptions = _prescriptions
        return self.prescriptions

    @property
    def _value_results(self):
        value_prescriptions = [prescription for prescription in self._prescriptions
                               if (len(self.value) > 1 and self.value in prescription.description.lower()) or
                               (len(self.value) == 1 and prescription.description.lower()[:1] == self.value)]
        return value_prescriptions

    @property
    def _value_fuzzy_results(self):
        if not self.value_fuzzy:
            return []

        value_fuzzy_prescriptions = [prescription for prescription in self._prescriptions
                               if prescription.fuzzy.startswith(self.value_fuzzy)]

        return value_fuzzy_prescriptions
