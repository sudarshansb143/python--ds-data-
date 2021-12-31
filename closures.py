
def outer_func(name):
    # closure function
    def inner_func():
        final_name = name + "ZZZZ"
        return "Greeting is {0}".format(final_name)
    
    # return function
    return inner_func


val = outer_func("Jasmine")
# print(val())

""" Lambda functions  """
stairs = ['thud', 'meow', 'thud', 'hiss']

def mapList (target, func ):
    new_target = []
    for i in target:
        temp = func(i)
        new_target.append(temp)
    return new_target

def capit(name) :
    return name.capitalize() + ">>>"
print(mapList(stairs, capit))



