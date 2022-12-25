import fileinput
import math

s2d = {"-": "-1", "=": "-2"}
d2s = {v: k for k, v in s2d.items()}


def snafu_to_decimal(snafu):
    s = 0
    for i, c in enumerate(snafu[::-1]):
        p = 5**i
        m = int(s2d.get(c, c))
        s += p * m

    return s


def decimal_to_snafu(decimal):
    snafu = ["0"] * 50
    rem = decimal
    while rem:
        p = math.log(abs(rem), 5)
        p = round(p)
        v = round(rem / (5**p))
        if v == 0:
            p -= 1
            v = round(rem / (5**p))

        snafu[-p - 1] = str(v)
        rem -= (5**p) * v

    s = "".join(d2s.get(s, s) for s in snafu)
    return s.lstrip("0")


total = sum(snafu_to_decimal(l.strip()) for l in fileinput.input())
print(decimal_to_snafu(total))
