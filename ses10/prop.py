# prop.py

# In python everything is public

class Person:
    def __init__(self):
        self.name = 'Tobias' #public instans variable
        self._age = 23

    def set_age(self, age):
        if age < 0:
            print ("Age cannot be negative")
        else: 
            self.age = age


    def get_age(self):
        return self._age




# We have looked at:
# * instance variable
# * Class Variables
# * methods
#   * datammodel methods

# Now we look at properties
