# prop.py

# In python everything is public

class Person:
    
    def __init__(self):
        self.name = 'Claus' # public instans variable
        self._age = 12
        self._gender = 'Male' # ppublic variable skift til en property


    @property  # getter
    def gender(self):
         return self._gender

    """
    @gender.setter  # setter
    def gender(self, x):
        if x in ['male', 'female']:
            self._gender = x

    """





    def set_age(self, age):
        if age < 0:
            print('No no no')
        else:
            self._age = age

    def get_age(self):
        return self._age


    x = property(get_age, set_age)
