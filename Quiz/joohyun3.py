tp = ('복숭아', '딸기', '무화과')

def tuple_change(tp, i, str):
    test = list(tp)
    test[i] = str
    return tuple(test)

tp = tuple_change(tp, 1, '오디')

print(tp)