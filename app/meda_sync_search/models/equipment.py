from app.meda_sync_search.models.model import Model


class Equipment(Model):
    def __init__(self, *,
                 description='',
                 hcpcs='',
                 average_cost=0,
                 category='',
                 modifier=''):
        super().__init__(description=description)

        self.hcpcs = hcpcs
        self.average_cost = average_cost
        self.category = category
        self.modifier = modifier

    def __eq__(self, other):
        is_equal = self.description == other.description \
                   and self.hcpcs == other.hcpcs \
                   and self.average_cost == other.average_cost \
                   and self.category == other.category \
                   and self.modifier == other.modifier

        return is_equal

    def __hash__(self):
        return super().__hash__()
