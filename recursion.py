def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def sum_recursion(n):
    if n == 0:
        return 0
    else:
        return n + sum_recursion(n - 1)


def sum_function(n):
    """321 -> 3+2+1"""

    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sum_function(n // 10)


def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output


def reverse_string(s):
    if len(s) == 1:
        return s

    return s[-1] + reverse_string(s[:-1])


def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, let in enumerate(s):
            # print(i, let, out)
            for perm in permute(s[:i] + s[i + 1:]):
                print(
                    f'perm je {perm} LET JE {let} AUT JE {out} -------------> {[let + perm]}---------->{out + [let + perm]}')
                out += [let + perm]

    return out


def fib_rec(n):
    if n == 0 or n == 1:
        return n

    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def rec_coin(target, coins):

    min_coins = target

    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c < target]:
            num_coins = 1 + rec_coin(target - i, coins)

            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins