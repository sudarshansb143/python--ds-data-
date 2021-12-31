
class GreetHim: 

    def __init__(self, name) -> None:
        self.name = name

    def print_greet(self):
        return "Greetiing is presented to {0}".format(self.name)



g1 = GreetHim("Samual")
    
print(g1.print_greet())