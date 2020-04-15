def input_number(n):
    if n.isnumeric() and int(n) >= 0:
        return True
    return False


def leo(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return leo(n - 1) + leo(n - 2) + 1

if __name__ == "__main__":
    print("Программа, определяющая n-ное число Леонардо ")
    print("Для выхода из программы введите 'Exit' ")

    n = 'A'
    while n != 'Exit':
        n = input("Введите n: ")
        number = input_number(n)
        if not number:
            if n == 'Exit':
                print("До новых встреч!")
                break
            else:
                print("Incorrect input")
        else:
            res = leo(int(n))
            print(n, "-ое число Леонардо равно", res)



