from enum import Enum
import warnings


class COLOR(Enum):
    BLACK = 1
    RED = 2


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            warnings.warn("Name has to be a string")

    @color.setter
    def color(self, value):
        if isinstance(value, COLOR):
            self._color = value
        else:
            warnings.warn("Color picking is only COLOR.BLACK or COLOR.RED")