from collections import deque

def bfs():
        while queue:
            row, col, brk = queue.popleft()
            for i in range(4):
                test_r = row + drow[i]
                test_c = col + dcol[i]
                if 0 <= test_r < N and 0 <= test_c < M:
                    if test_r == ex - 1 and test_c == ey - 1:
                        if brk == 1:
                            return visited[row][col][1]
                        else:
                            return visited[row][col][0]
                    else:
                        if brk == 1:
                            if visited[test_r][test_c] == [0,0] and map_list[test_r][test_c] == 0:
                                visited[test_r][test_c][1] = visited[row][col][1] + 1
                                queue.append((test_r,test_c,brk))
                        else:
                            if visited[test_r][test_c] == [0,0] and map_list[test_r][test_c] == 1:
                                visited[test_r][test_c][1] = visited[row][col][0] + 1
                                queue.append((test_r, test_c, brk + 1))
                            elif visited[test_r][test_c][0] == 0 and map_list[test_r][test_c] == 0:
                                visited[test_r][test_c][0] = visited[row][col][0] + 1
                                queue.append((test_r, test_c, brk))
        return -1

N, M = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
brake = 0
queue = deque()
queue.append((hx-1, hy-1, brake))
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
visited[hx-1][hy-1] = [1,0]

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

ans = bfs()
print(ans)