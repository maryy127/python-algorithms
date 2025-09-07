def init(pref):
    pref[0][0] = arr[0][0]
    for i in range(1, n):
        pref[i][0] = pref[i - 1][0] + arr[i][0]
    for j in range(1, m):
        pref[0][j] = pref[0][j - 1] + arr[0][j]
    for i in range(1, n):
        for j in range(1, m):
            pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + arr[i][j]
    return pref 

def gen_sum(x1, y1, x2, y2):
    if x1 == 0 and y1 == 0:
        return pref[x2][y2]
    if y1 == 0:
        return pref[x2][y2] - pref[x1 - 1][y2]
    if x1 == 0:
        return  pref[x2][y2] - pref[x2][y1 - 1]
    return pref[x2][y2] - pref[x2][y1 - 1] - pref[x1 - 1][y2] + pref[x1 - 1][y1 - 1]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
ys = [[0] * m for i in range(n)]
pref = init(ys)
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    print(gen_sum(x1 - 1, y1 - 1, x2 - 1, y2 - 1))