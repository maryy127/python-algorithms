def init(arr, n):
  pref = [0] * (n + 1)
  pref[0] = arr[0]
  for i in range(1, n):
    pref[i] = pref[i - 1] + arr[i]
  return pref

def get_sum(l, r):
  if l == 0:
    return pref[r]
  return pref[r] - pref[l - 1]

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pref = init(arr, n)
for i in range(m):
  l, r = map(int, input().split())
  l, r = l - 1, r - 1
  print(get_sum(l, r))