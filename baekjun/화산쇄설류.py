from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def iswall(x,y):
    if x < 0 or x >= M:
        return False
    if y < 0 or y >= N:
        return False
    return True

M, N, V = map(int, input().split())
X, Y = map(int, input().split())
height = [list(map(int,input().split())) for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
visited2 = [[0 for _ in range(N)] for _ in range(M)]
queue = deque()
for _ in range(V):
    x, y, t = map(int,input().split())
    visited[x-1][y-1] = t
    queue.append((x-1,y-1,t))

queue2 = deque()
queue2.append((X-1,Y-1,0))
visited[X-1][Y-1] = -1
mx = height[X-1][Y-1]
ans_t = 0
time = 0
while queue:

    for _ in range(len(queue)):
        x, y, t = queue.popleft()
        if t > time:
            queue.append((x,y,t))
        else:
            for i in range(4):
                test_x = x + dx[i]
                test_y = y + dy[i]
                if iswall(test_x, test_y):
                    if (visited[test_x][test_y] == 0 or visited[test_x][test_y] > t+1) and visited2[test_x][test_y] == 0:
                        visited[test_x][test_y] = t+1
                        queue.append((test_x,test_y,t+1))

    time += 1

    for _ in range(len(queue2)):
        x, y, t = queue2.popleft()
        for i in range(4):
            test_x = x + dx[i]
            test_y = y + dy[i]
            if iswall(test_x, test_y):
                if visited[test_x][test_y] == 0 and visited2[test_x][test_y] == 0:
                    visited2[test_x][test_y] = t + 1
                    queue2.append((test_x, test_y, t + 1))
                    h = height[test_x][test_y]
                    if h > mx:
                        mx = h
                        ans_t = t+1
                    elif h == mx and ans_t > t+1:
                        ans_t = t+1
print(mx,ans_t)