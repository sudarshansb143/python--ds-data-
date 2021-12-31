# this is duck typing I don't know what it is


class BablingDuck:
    def __init__(self, name) -> None:
        self.name = name

    def who(self):
        return(f"Babbling {self.name}")

    def says(self):
        return(f"Bubble {self.name}")


b1 = BablingDuck("Sam")
b3 = BablingDuck("Jonathan")
b2 = BablingDuck("Parkins")


def who_says(obj):
    print(f"Who is {obj.who()} and says is {obj.says()}")


who_says(b1)
who_says(b2)
who_says(b3)

print(b1.__eq__(b2))