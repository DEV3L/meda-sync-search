import hashlib
import json

from app.meda_sync_search.transformers.str_transformer import StrTransformer


class Model:
    def __init__(self, *, description=''):
        self.description = description
        self.fuzzy = StrTransformer(self.description).fuzzy

    def serialize(self):
        return self._json

    @property
    def _json(self):
        return json.dumps(self.__dict__).encode()

    def __repr__(self):
        return self._json

    def __hash__(self):
        return int(hashlib.sha1(self._json).hexdigest(), 16)
