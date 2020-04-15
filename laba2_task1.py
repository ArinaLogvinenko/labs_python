import math

def input_number(message):
  while True:
    try:
       user_input = int(input(message))
    except ValueError:
       print("Incorrect input")
       continue
    else:
       return user_input
       break


def get_and_validate_array_from_input():
    print("Enter array")
    try:
        arr = list(map(float, input().split()))
    except ValueError:
        print("Incorrect input")
        exit(1)
    return arr


def get_and_validate_array_from_file(filename):
    arr = []
    with open(filename, "r") as file:
        for line in file:
            try:
                kek = list(map(float, line.split()))
                arr.extend(kek)
            except ValueError:
                print("Incorrect input")
                exit(1)
    return arr


def sum_of_array(arr, l, r):
    length = len(arr)
    mysum = 0
    new_length = math.ceil(math.sqrt(length))
    new_arr = [0] * new_length

    for i in range(length):
        new_arr[i // new_length] += arr[i]


    while l <= r:
        if l % new_length == 0 and l + new_length - 1 <= r:
            mysum += new_arr[l // new_length]
            l += new_length
        else:
            mysum += arr[l]
            l += 1
    return mysum


if __name__ == "__main__":
    print("Программа, реализующая метод sqrt-декомпозиции для суммы на отрезке массива от l до r")

    l = input_number("Введите l: ")
    r = input_number("Введите r: ")

    print("Выберите способ ввода данных")
    print("1. Ввод из командной строки")
    print("2. Ввод из файла")
    case = int(input())
    if case == 1:
        arr = get_and_validate_array_from_input()
        result = sum_of_array(arr, l, r)
        print(result)
    elif case == 2:
        array = get_and_validate_array_from_file("text.txt")
        result = sum_of_array(array, l, r)
        print(result)
    else:
        exit(1)