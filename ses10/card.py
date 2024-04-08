class Card:
    def __init__(self, face, value):
        self._face = face
        self._value = value

    @property
    def face(self):
        return self._face

    @face.setter
    def face(self, x):
        raise ValueError('Object is Imutable!')

    @property
    def value(self):
        return self._value
