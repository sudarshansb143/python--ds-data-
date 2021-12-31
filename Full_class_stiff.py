class MainClass:
    count = 0
    def __init__(self, hidden_name) -> None:
        self.hidden_name = hidden_name
        MainClass.count += 1

    @property
    def name(self):
        print("Inside gettter")
        return self.hidden_name

    @name.setter
    def set_name(self, name):
        print("Inside settter")
        self.hidden_name = name


    @classmethod
    def print_class_count(cls):
        print(f"Class count is {cls.count}")

    @staticmethod
    def print_static():
        print("This is  static method")




m1 = MainClass("Samurai")
m2 = MainClass("Sami")

m1.hidden_name = "Jamine"

print(m1.hidden_name)

MainClass.print_class_count()

MainClass.print_static()