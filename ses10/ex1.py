#Ex 1: create a car class

class Car:
    def __init__(self, make, model, bhp, mph):
        self._make = make
        self._model = model
        self._bhp = bhp
        self._mph = mph

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if not value:
            raise ValueError("Make cannot be empty")
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not value:
            raise ValueError("Model cannot be empty")
        self._model = value

    @property
    def bhp(self):
        return self._bhp

    @bhp.setter
    def bhp(self, value):
        if value <= 0:
            raise ValueError("bhp must be greater than 0")
        self._bhp = value

    @property
    def mph(self):
        return self._mph

    @mph.setter
    def mph(self, value):
        if value <= 0:
            raise ValueError("mph must be greater than 0")
        self._mph = value

# Example of using the class
car_example = Car(make="Audi", model="A4", bhp=240, mph=155)

print(car_example.make, car_example.model, car_example.bhp, car_example.mph)

