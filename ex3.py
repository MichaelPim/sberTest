"""3) В этом задании мы хотим преобразовать строку в целое число. Строки просто представляют числа словами.

Примеры:

"один" => 1
"двадцать" => 20
"двести сорок шесть" => 246
"семьсот восемьдесят три тысячи девятьсот девятнадцать" => 783919
Дополнительные замечания:

Минимальное число - «ноль» (включительно)
Максимальное количество, которое должно поддерживаться - 1 миллион (включительно).
Все проверенные числа действительны, вам не нужно их подтверждать
"""

from __future__ import print_function
import sys

russian_number_system = {
    'ноль': 0,
    'один': 1,
    'одна': 1,
    'два': 2,
    'две': 2,
    'три': 3,
    'четыре': 4,
    'пять': 5,
    'шесть': 6,
    'семь': 7,
    'восемь': 8,
    'девять': 9,
    'десять': 10,
    'одиннадцать': 11,
    'двенадцать': 12,
    'тринадцать': 13,
    'четырнадцать': 14,
    'пятнадцать': 15,
    'шестнадцать': 16,
    'семнадцать': 17,
    'восемнадцать': 18,
    'девятнадцать': 19,
    'двадцать': 20,
    'тридцать': 30,
    'сорок': 40,
    'пятьдесят': 50,
    'шестьдесят': 60,
    'семьдесят': 70,
    'восемьдесят': 80,
    'девяносто': 90,
    'сто': 100,
    'двести': 200,
    'триста': 300,
    'четыреста': 400,
    'пятьсот': 500,
    'шестьсот': 600,
    'семьсот': 700,
    'восемьсот': 800,
    'девятьсот': 900,
    'тысяча': 1000,
    'тысяч': 1000,
    'тысячи': 1000,
    'миллион': 1000000,
    'миллиард': 1000000000
}


def form_number(number_words):
    if isinstance(number_words, str):
        words = number_words.strip().split()
    else:
        words = number_words
    words_without_numbers = []
    numbers = []
    i = 0
    for ind, word in enumerate(words):
        if word in russian_number_system.keys():
            if i == 0:
                i += ind
            numbers.append(russian_number_system[word])
        else:
            words_without_numbers.append(word)

    if len(numbers) == 0:
        return " ".join(words)

    elif len(numbers) == 6:
        if numbers[2] == 1000:
            integer = str((numbers[0] + numbers[1]) * numbers[2] + numbers[3] + numbers[4] + numbers[5])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        else:
            integer = str((numbers[0] + numbers[1] + numbers[2]) * numbers[3] + numbers[4] + numbers[5])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
    elif len(numbers) == 5:
        if numbers[2] == 1000:
            integer = str((numbers[0] + numbers[1]) * numbers[2] + numbers[3] + numbers[4])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        else:
            integer = str((numbers[0] * numbers[1]) + numbers[2] + numbers[3] + numbers[4])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
    elif len(numbers) == 4:
        if numbers[0] == 1000:
            integer = str(numbers[0] + numbers[1] + numbers[2] + numbers[3])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        elif numbers[0] < 100 and numbers[1] < 10 and numbers[2] < 100 and numbers[3] < 10:
            integer = str(numbers[0] + numbers[1]) + str(numbers[2] + numbers[3])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        else:
            integer = str(numbers[0] * numbers[1] + numbers[2] + numbers[3])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
    elif len(numbers) == 3:
        if numbers[1] == 1000:
            integer = str(numbers[0] * numbers[1] + numbers[2])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        elif numbers[1] == 0:
            integer = str(numbers[0]) + str(numbers[1]) + str(numbers[2])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        elif numbers[0] < 20:
            integer = str(numbers[0]) + str(numbers[1] + numbers[2])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        elif numbers[2] < 20 and numbers[1] < 10:
            integer = str(numbers[0] + numbers[1]) + str(numbers[2])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        elif numbers[0] >= 100 and numbers[2] < 20 and numbers[1] > 10:
            integer = str(numbers[0] + numbers[1] + numbers[2])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        elif numbers[2] < 20 and numbers[1] > 10:
            integer = str(numbers[0]) + str(numbers[1] + numbers[2])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        else:
            integer = str(numbers[0] + numbers[1] + numbers[2])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
    elif len(numbers) == 2:
        if numbers[1] == 1000:
            integer = str(numbers[0] * numbers[1])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        elif numbers[0] <= 20 and 10 <= numbers[1] <= 20:
            integer = str(numbers[0]) + str(numbers[1])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
        else:
            integer = str(numbers[0] + numbers[1])
            words_without_numbers.insert(i, integer)
            return " ".join(words_without_numbers)
    else:
        print(numbers)
        integer = str(numbers[0])
        words_without_numbers.insert(i, integer)
        return " ".join(words_without_numbers)


if __name__ == "__main__":
    string = sys.argv[0]
    print(form_number(input()))
