# classes A
''' classes A '''

# https://docs.python.org/3/tutorial/classes.html
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

class Wolf:
    def __init__(self, name):
        self.name = name
        
    def give_name(self):
        print(name)