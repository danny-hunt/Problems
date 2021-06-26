def fizzbuzz_naive(n):
    for number in range(1, n+1):
        output = ""
        if number % 3 == 0:
            output += "fizz"
        if number % 5 == 0:
            output += "buzz"
        if not output:
            output += str(number)
        print(output)


def fizzbuzz_recurse(n, array=[]):
    if n % 3 == 0:
        if n % 5 == 0:
            array.append("fizzbuzz")
        else:
            array.append("fizz")
    elif n % 5 == 0:
        array.append("buzz")
    else:
        array.append(n)

    if n == 1:
        for entry in reversed(array):
            print(entry)
    else:
        fizzbuzz_recurse(n-1, array)


import json
import random
import urllib.request


def fizzbuzz3(n, *args):
    words = ["fizz", "buzz", "wang", "bang", "cough"]
    factors = [factor for factor in args]
    factor_words = {}
    url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
    word_list = json.loads(url.read())
    for index, factor in enumerate(factors):
        if index < 5:
            factor_words[str(factor)] = words[index]
        else:
            factor_words[str(factor)] = random.choice(word_list)

    for number in range(1,n+1):
        output = "".join(
            factor_words[str(factor)]
            for factor in factors
            if number % factor == 0
        )

        if len(output) == 0:
            output += str(number)
        print(output)


fizzbuzz_naive(100)
fizzbuzz_recurse(100)
fizzbuzz3(100, 2, 3, 5, 7, 11, 6)
