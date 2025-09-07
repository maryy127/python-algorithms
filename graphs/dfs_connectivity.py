def dfs(v):
  used[v] = 1
  for u in gr[v]:
    if used[u] != 1:
      dfs(u)

n, m = map(int, input().split())
gr = [[] for i in range(n)]
used = [0] * n 
for i in range(m):
  v, u = map(int, input().split())
  v -= 1
  u -= 1
  gr[v].append(u)
  gr[u].append(v)
c = 0  
for v in range(n):
  if used[v] == 0:
    dfs(v)
    c += 1
print(c)