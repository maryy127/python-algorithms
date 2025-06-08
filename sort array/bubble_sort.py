a = int(input())
ar = list(map(int, input().split()))

for i in range(a - 1):
    for j in range(a - 1 - i):
        if ar[j] > ar[j + 1]:
            ar[j], ar[j + 1] = ar[j + 1], ar[j]
            
print(ar)