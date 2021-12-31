def handle_it():
    try:
        print(10 / 0)
    except ZeroDivisionError as e:
        print(e)

handle_it()