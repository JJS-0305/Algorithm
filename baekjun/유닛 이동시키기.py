from _collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def possible(row,col):
    global visited
    for i in range(A):
        for j in range(B):
            if 0 <= row + i < N and 0 <= col + j < M:
                if map_list[row+i][col+j] == 1:
                    return False
            else:
                return False
    visited[row][col] = 1
    return True

def bfs(row, col):
    global visited
    queue = deque()
    queue.append((row,col,0))
    visited[row][col] = 1

    while queue:
        r, c, cnt = queue.popleft()
        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if 0 <= test_r < N and 0 <= test_c < M:
                if visited[test_r][test_c] == 0:
                    if possible(test_r,test_c):
                        queue.append((test_r,test_c, cnt+1))
                elif visited[test_r][test_c] == 2:
                    return cnt + 1
    return -1

N, M, A, B, K = map(int, input().split())
map_list = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    map_list[r-1][c-1] = 1

st_r, st_c = map(int, input().split())
for r in range(A):
    for c in range(B):
        map_list[st_r-1+r][st_c-1+c] = 2

ed_r, ed_c = map(int, input().split())
visited[ed_r-1][ed_c-1] = 2

ans = bfs(st_r-1, st_c-1)
print(ans)