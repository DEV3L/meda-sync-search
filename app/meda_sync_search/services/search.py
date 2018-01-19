from app.meda_sync_search.transformers.str_transformer import StrTransformer


class Search:
    def __init__(self, value, items):
        self._value = value or ''
        self.value = self._value.lower()
        self.value_fuzzy = StrTransformer(self._value).fuzzy

        self._items = items if items != None else []
        self.items = None if value else items

    @property
    def results(self):
        if self.items:
            return self.items

        _items = self._value_results
        _items.extend(self._value_fuzzy_results)
        _items = list(set(_items))
        _items.sort(key=lambda item: item.description)

        self.items = _items
        return self.items

    @property
    def _value_results(self):
        value_items = [item for item in self._items
                       if (len(self.value) > 1 and self.value in item.description.lower()) or
                       (len(self.value) == 1 and item.description.lower()[:1] == self.value)]
        return value_items

    @property
    def _value_fuzzy_results(self):
        if not self.value_fuzzy:
            return []

        value_fuzzy_items = [item for item in self._items
                             if item.fuzzy.startswith(self.value_fuzzy)]

        return value_fuzzy_items
