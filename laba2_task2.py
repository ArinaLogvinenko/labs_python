import random
import string
import sys


def main():
    filename = input('Filename ') + '.txt'
    print(filename)
    Mb = int(input('Size of file '))
    B = Mb * 1048576
    K = tuple(input('Count of words in string ').split(' '))
    L = tuple(input('Length of word ').split(' '))
    res = ''

    def words_generation(length_of_word):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length_of_word))

    with open(filename, 'w') as opened_file:
        while sys.getsizeof(res) <= B:
            count_of_words = random.randint(int(K[0]), int(K[1]))
            for word in range(count_of_words):
                length_of_word = random.randint(int(L[0]), int(L[1]))
                word = words_generation(length_of_word)
                if sys.getsizeof(res) + sys.getsizeof(word) > B:
                    break
                else:
                    res += word + ' '
            res += '\n'
        opened_file.write(res)


if __name__ == "__main__":
    main()



