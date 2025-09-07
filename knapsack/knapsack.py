n, m = map(int, input().split())
w = list(map(int, input().split()))
indx = [0]
dp = [1] + [0] * m
for i in range(n):
  for j in range(m - w[i], -1, -1):
    if dp[j] == 1:
      dp[j + w[i]] = 1
      indx.append(j + w[i])
print(max(indx))