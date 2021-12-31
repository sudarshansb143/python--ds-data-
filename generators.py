
# Generator function
def generateSequence(start=0, stop = 10):
    while start < stop:
        yield start
        start +=1

# consumption of generator
for i in generateSequence():
    print(i, end="<>")