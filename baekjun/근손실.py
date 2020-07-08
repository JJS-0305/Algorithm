def possible_plan(n,r,w):
    global cnt
    global visited

    if n == r:
        cnt += 1
    else:
        for i in range(N):
            if visited[i] == 0 and w + kits[i] - K >= 500:
                visited[i] = 1
                possible_plan(n,r+1, w+kits[i] - K)
                visited[i] = 0

N, K = map(int, input().split())
kits = list(map(int, input().split()))
visited = [0 for _ in range(N)]
cnt = 0

possible_plan(N,0,500)
print(cnt)