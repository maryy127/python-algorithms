n = int(input())
x = 300000
A = []
prime = [0, 0] + [1] * x
for i in range(2, x + 1):
    if prime[i]:
        A.append(i)
        if len(A) == n:
            print(A[-1])
            exit()
        for j in range(2 * i, x + 1, i):
            prime[j] = 0
    