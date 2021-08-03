class Geek:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x

raj = Geek()

raj.set_age(21)
  
print(raj.get_age())
  
print(raj._age)