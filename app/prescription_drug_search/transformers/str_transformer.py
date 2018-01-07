import fuzzy

class StrTransformer:
    def __init__(self, _str):
        self._str = _str

    @property
    def fuzzy(self):
        return fuzzy.nysiis(self._str)
