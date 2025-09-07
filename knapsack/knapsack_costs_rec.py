n, m = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[-1, []] for i in range(m + 1)]
dp[0] = [0, []]
for i in range(n):
  for j in range(m - w[i], -1, -1):
    if dp[j][0] != -1 and dp[j][0] + c[i] > dp[j + w[i]][0]:
      dp[j + w[i]][0] = dp[j][0] + c[i]
      dp[j + w[i]][1] = dp[j][1] + [i + 1]
maxi = -1
ans = []
for i in range(m + 1):
  if dp[i][0] > maxi:
    maxi = dp[i][0] 
    ans = dp[i][1]

print(*ans)