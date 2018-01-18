class DataTransformer:
    def __init__(self, data: dict):
        self.data = data

    def _get_value(self, key: str):
        return self.data[key].strip()
