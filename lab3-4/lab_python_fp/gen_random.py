import random

def gen_random(num_count, begin, end):
    assert num_count > 1
    arr = []
    for i in range(num_count):
        arr.append(random.randrange(begin, end + 1))
    print(*arr, sep = ", ")
    return arr
