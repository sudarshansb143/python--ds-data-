animal = "FruitBat"

def access_global():
    # accessing and modifying the global variables
    global animal
    animal =  "Jaspire"
    print("val of animal is {0} nd id is {1} ".format(animal, id(animal)))

access_global()

print("anni ", animal)
print("id >", id(animal))


