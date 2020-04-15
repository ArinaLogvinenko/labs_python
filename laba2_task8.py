def input_number(n):
    if n.isnumeric() and int(n) >= 0:
        return True
    return False

def powerOfTwo(n):
    if (n <= 0):
        return False
    if (n == 1):
        return True
    while n != 1:
        if (n % 2 == 1):
            return False
        n = n // 2
    return True

if __name__ == "__main__":
    print("Программа, определяющая является ли введенное число n степенью двойки")
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
            if powerOfTwo(int(n)):
                print(n, 'является степенью двойки')
            else:
                print(n, 'не является степенью двойки')
