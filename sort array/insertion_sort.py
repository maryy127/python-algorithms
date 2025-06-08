n = int(input())
arr = list(map(int, input().split()))

for j in range(1, n):
    i = j
    while i > 0 and arr[i] < arr[i - 1]:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i -= 1
        
print(arr)