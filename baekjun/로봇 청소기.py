from collections import deque
from sys import stdin
input = stdin.readline

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

def iswall(row, col):
    if row < 0 or row >= h:
        return False
    if col < 0 or col >= w:
        return False
    return True

def bfs(robot):
    while robot:
        status, row, col, d = robot.popleft()
        for i in range(4):
            test_r = row + drow[i]
            test_c = col + dcol[i]
            if iswall(test_r,test_c):
                if map_list[test_r][test_c] == 'o' or map_list[test_r][test_c] == '.':
                    if visited[test_r][test_c][status] == 0:
                        visited[test_r][test_c][status] = 1
                        robot.append((status, test_r, test_c, d+1))
                elif type(map_list[test_r][test_c]) == int:
                    next_status = status | (map_list[test_r][test_c])
                    if visited[test_r][test_c][next_status] == 0:
                        visited[test_r][test_c][status] = 1
                        visited[test_r][test_c][next_status] = 1
                        robot.append((next_status, test_r, test_c, d+1))

                        if next_status == 2**(cnt)-1:
                            return d+1
    return -1

while True:
    w, h = map(int, input().split())
    if (w, h) == (0,0):
        break
    map_list = [list(input()) for _ in range(h)]

    cnt = 0
    st_r, st_c = -1, -1
    for i in range(h):
        for j in range(w):
            if map_list[i][j] == '*':
                map_list[i][j] = 2**cnt
                cnt += 1
            if map_list[i][j] == 'o':
                st_r, st_c = i, j
    status = 0
    visited = [[[0 for _ in range(2**cnt)] for _ in range(w)] for _ in range(h)]
    visited[st_r][st_c][status] = 1

    d = 0
    robot = deque()
    robot.append((status, st_r, st_c, d))


    ans = bfs(robot)
    print(ans)