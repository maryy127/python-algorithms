n = int(input())
a = list(map(int, input().split()))
dp = [1] * n
prev = [-1] * n
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

ans = []
ind = dp.index(max(dp))
while ind != -1:
    ans.append(a[ind])
    ind = prev[ind]
    
ans.reverse()
print(len(ans))
print(*ans)