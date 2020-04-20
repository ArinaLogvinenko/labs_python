k = [5, 32, ['python'], [2, [2,['kek'], [1, 3]], 12, [2, [9,73]]]]


def flat_it(x):
    for i in range(0, len(x)):
        if (type(x[i]) != list):
            arr.append(x[i])
            continue
        flat_it(x[i])


if __name__ == "__main__":
    try:
        arr = []
        flat_it(k)
        print(arr)
    except ValueError:
        print('Value Error')
