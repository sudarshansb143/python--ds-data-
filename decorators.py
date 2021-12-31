def document_it(func):
    def new_function(*args, **kwargs):
         print('Running function:', func.__name__)
         print('Positional arguments:', args)
         print('Keyword arguments:', kwargs)
         result = func(*args, **kwargs)
         print('Result:', result)
         return result
    return new_function

def add_nums(a,b):
    return a + b 

new_func = document_it(add_nums)

# new_func(10, 20)


"""Alternative usage """

@document_it
def multiply (a, b):
    return a * b


multiply(10, 20)