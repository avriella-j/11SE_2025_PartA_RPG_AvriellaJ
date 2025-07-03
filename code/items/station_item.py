
class StationItem:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def examine(self):
        return self._description