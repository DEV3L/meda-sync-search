from app.meda_sync_search.services.logging_service import LoggingService
from app.meda_sync_search.transformers.str_transformer import StrTransformer

logger = LoggingService('search')

class Search:
    def __init__(self, value, items):
        self._value = value or ''
        logger.info(f'Search value: {value}')

        self.value = self._value.lower()
        self.value_fuzzy = StrTransformer(self._value).fuzzy if len(self._value) > 1 else ''

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
        if len(self.value) == 1:
            return [item for item in self._items if item.description.lower()[:1] == self.value]

        value_items = []

        for token in self.value.split():
            value_items.extend([item for item in self._items if token in item.description.lower()])

        return value_items

    @property
    def _value_fuzzy_results(self):
        if not self.value_fuzzy:
            return []

        value_fuzzy_items = [item for item in self._items
                             if item.fuzzy.startswith(self.value_fuzzy)]

        return value_fuzzy_items
