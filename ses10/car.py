class Car:


    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    @property
    def make(self):
        return self._make 

    @make.setter
    def make(self, make):
        if make in ['Volvo', 'Bmw']:
            self._make = make
        else:
            print('No no no')
