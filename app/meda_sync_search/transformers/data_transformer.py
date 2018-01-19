class DataTransformer:
    def __init__(self, data: dict):
        self.data = data

    def _get_value(self, key: str):
        return self.data[key].strip()

    def _get_float(self, key: str):
        value = self._get_value(key)

        for ignore_character in float_ignore_characters:
            value = value.replace(ignore_character, '')

        float_value = float(value.strip()) if value else 0.0

        return float_value


float_ignore_characters = ['$', '-', '"', ',']
