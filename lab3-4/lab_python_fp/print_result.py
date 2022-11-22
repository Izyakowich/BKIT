def print_result(funct):
    def wrapper():
        print(funct.__name__)
        if isinstance(funct(), list):
           print(*funct(), sep = "\n")

        elif isinstance(funct(), dict):
            temp = funct()
            for i in temp:
                print(i, temp.get(i), sep = " = ")

        else:
            print(funct())
    return wrapper

@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]
