# usage of magic methods

class Magic:
    def __init__(self,num) -> None:
        self.num = num

    def __eq__(self, __o: object) -> bool:
        return self.num == __o.num


m1 = Magic(10)

m2 = Magic(20)

print(m1.__eq__(m2))