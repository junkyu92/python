a = [22, 44, 66, 11, 99]

def maximum(*array):
    m = 0
    for i in range(0, len(a)):
        if m < a[i]:
            m = a[i]
    return m

print(int(maximum(a)))
