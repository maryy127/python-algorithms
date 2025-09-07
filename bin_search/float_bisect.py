from math import sqrt


def f(x):
    return x ** 2 + sqrt(x)


def binf(l, r, a):
    for i in range(100):
        mid = (l + r) / 2
        if f(mid) < a:
            l = mid
        else:
            r = mid
    return r


a = float(input())
print(round(binf(1.0, 100000.0, a), 6))