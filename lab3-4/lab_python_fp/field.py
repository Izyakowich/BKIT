def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        arr = []
        for i in items:
            temp_key = i.get(args[0], "None")
            if temp_key != "None":
                arr.append(temp_key)
        return arr
    else:
        arr = []
        for i in items:
            temp = {}
            for key in args:
                temp_key = i.get(key, "None")
                if temp_key != "None":
                    temp.update({key: temp_key})
            arr.append(temp)
        print(*arr, sep = ", ")