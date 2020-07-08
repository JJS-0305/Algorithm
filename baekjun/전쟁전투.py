drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

def iswall(row, col):
    if row < 0 or row >= M:
        return False
    if col < 0 or col >= N:
        return False
    return True

def dfs(row, col, clr):
    global visited
    cnt = 1
    for i in range(4):
        test_r = row + drow[i]
        test_c = col + dcol[i]
        if iswall(test_r, test_c):
            if visited[test_r][test_c] == 0 and solidiers[test_r][test_c] == clr:
                visited[test_r][test_c] = 1
                cnt += dfs(test_r, test_c, clr)

    return cnt

N, M = map(int, input().split())
solidiers = [input() for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]
blue = 0
white = 0

for r in range(M):
    for c in range(N):
        if solidiers[r][c] == 'W' and visited[r][c] == 0:
            visited[r][c] = 1
            white += (dfs(r,c,'W'))**2
        if solidiers[r][c] == 'B' and visited[r][c] == 0:
            visited[r][c] = 1
            blue += (dfs(r,c,'B'))**2
print(white, blue)