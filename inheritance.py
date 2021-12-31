class Parent:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Name is ", self.name)

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    
c = Child("Samual")

c.print_name()