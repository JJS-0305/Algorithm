import heapq

def make_edge():
    for i in range(N):
        for j in range(i+1,N):
            d = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)*E
            heapq.heappush(distance, (d,i,j))

def find_set(v):
    if v == p[v]:
        return p[v]
    return find_set(p[v])

def union(v,u):
    root1 = find_set(v)
    root2 = find_set(u)

    if root1 > root2:
        p[root1] = root2
    else:
        p[root2] = root1

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    p = [i for i in range(N)]
    distance = []
    make_edge()

    cnt = 0
    ans = 0
    while cnt != N-1:
        d, a, b = heapq.heappop(distance)
        if find_set(a) != find_set(b):
            ans += d
            cnt += 1
            union(a,b)
    ans = round(ans)
    print("#{} {}".format(tc, ans))