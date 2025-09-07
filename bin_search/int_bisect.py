def f(a):
    return a ** 3

def bin(r, l, x):
    while r - l > 1:
        mid = (r + l) // 2
        if f(mid) < x:
            l = mid
        else:
            r = mid
    return r


x = int(input())
print(bin(10**6, -1, x))
