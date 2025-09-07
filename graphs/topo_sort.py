def topple(v):
    used[v] = 1
    for u in sm_gr[v]:
        if used[u] == 0:
            topple(u)
        elif used[u] == 1:
            global cycle
            cycle += 1
            print('No')
            exit()
    used[v] = 2
    sort.append(v)
                                        
n, m = map(int, input().split())
sm_gr = [[] for i in range(n)]
for i in range(m):
    v, u = map(int, input().split())
    v-= 1
    u -= 1
    sm_gr[v].append(u)


used = [0] * n 

        
cycle = 0
sort = []
for u in range(n):
    if used[u] == 0:
        topple(u)
        
sort.reverse()
l = len(sort)
for i in range(l):
    sort[i] += 1
    
print('Yes')
print(*sort)