n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n):
    current_min = arr[i]
    min_index = i
    for j in range(i, n):
        if arr[j] < current_min:
            current_min = arr[j]
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)