n, m = map(int, input().split())
forward = [0] * (n+1)
visited = [0] * (n+1)
orders = [[] for _ in range(n+1)]

answer = []
for _ in range(m):
    a, b = map(int, input().split())
    orders[a].append(b)
    forward[b] += 1

visited[0] = 1

while len(answer) < n:
    for i in range(1,n+1):
        if visited[i] == 0 and forward[i] == 0:
            visited[i] = 1
            answer.append(str(i))
            while orders[i]:
                forward[orders[i].pop()] -= 1
print(' '.join(answer))