def merge(le, ri):
    l, r = 0, 0
    ans = []
    while l < len(le) and r < len(ri):
        if le[l] <= ri[r]:
            ans.append(le[l])
            l += 1
        else:
            ans.append(ri[r])
            r += 1
    while l < len(le):
        ans.append(le[l])
        l += 1
    while r < len(ri):
        ans.append(ri[r])
        r += 1
    return ans


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    le = merge_sort(arr[:mid])
    ri = merge_sort(arr[mid:])
    return merge(le, ri)


n = int(input())
arr = list(map(int, input().split()))

print(*merge_sort(arr))