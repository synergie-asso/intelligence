class Square:
    def __init__(self, v):
        self.value = v
        self.fusion = False

    def __int__(self):
        return self.value

    def __add__(self, other):
        return self.value + other

    def __mul__(self, other):
        return self.value * other

    def __float__(self):
        return float(self.value)

    def ___le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __str__(self):
        return str(self.value)
