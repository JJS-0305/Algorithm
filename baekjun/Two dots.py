from collections import deque

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= M:
        return False
    return True

def bfs(row, col, val):
    visited[row][col] = 1
    cycle = deque()
    cycle.append((row,col,val))

    while cycle:
        row, col, val = cycle.popleft()
        for i in range(4):
            test_r = row + drow[i]
            test_c = col + dcol[i]
            if iswall(test_r,test_c):
                if visited[test_r][test_c] == 0 and board[test_r][test_c] == val:
                    visited[test_r][test_c] = visited[row][col] + 1
                    cycle.append((test_r,test_c,val))
                elif visited[test_r][test_c] != 0 and board[test_r][test_c] == val:
                    if visited[test_r][test_c] == visited[row][col] + 1:
                        return 'Yes'
    return 'No'


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

ans = 'No'
for row in range(N):
    for col in range(M):
        if visited[row][col] == 0:
            if bfs(row, col, board[row][col]) == 'Yes':
                ans = 'Yes'
                break

print(ans)