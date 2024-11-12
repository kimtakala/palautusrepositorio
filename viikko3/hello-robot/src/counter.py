'info docstring'
class Counter:
    'info docstring'
    def __init__(self, initial_value=0):
        self._initial_value = initial_value
        self.value = initial_value

    def increase(self):
        'info docstring'
        self.value = self.value + 1

    def increment(self, amount):
        'info docstring'
        self.value = self.value + amount

    def decrease(self):
        'info docstring'
        self.value = self.value - 1

    def reset(self):
        'info docstring'
        self.value = self._initial_value
