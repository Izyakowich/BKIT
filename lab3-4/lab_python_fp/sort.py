def sort_arr(data):
    res = sorted(data, key = abs, reverse= True)
    print(res)

    lambda_res = sorted(data, key = lambda a : -abs(a))
    print(lambda_res)