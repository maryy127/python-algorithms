def bin(l, r, arr, x):
    while r - l > 1:
        mid = (r + l) // 2
        if arr[mid] < x:
            l = mid
        else:
            r = mid
    return r


n = int(input())
arr = list(map(int, input().split()))
check = int(input())

ind = bin(-1, len(arr), arr, check)
if ind != len(arr) and arr[ind] == check:
    print("YES")
