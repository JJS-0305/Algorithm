from collections import deque

drow = [-1,1,0,0]
dcol = [0,0,-1,1]

def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def min_distance(st_r, st_c):
    min = [N*N, -1, -1]
    if maplist[st_r][st_c] >= 11:
        return 0, st_r, st_c
    queue = deque()
    queue.append((st_r,st_c))
    while queue:
        now_r, now_c = queue.popleft()
        if visited[now_r][now_c] > min[0]:
            break
        for i in range(4):
            test_r = now_r + drow[i]
            test_c = now_c + dcol[i]
            if iswall(test_r,test_c) and visited[test_r][test_c] == 0:
                if maplist[test_r][test_c] != 1:
                    visited[test_r][test_c] = visited[now_r][now_c] + 1
                    if maplist[test_r][test_c] >= 11:
                        if visited[test_r][test_c] < min[0]:
                            min[0] = visited[test_r][test_c]
                            min[1],min[2] = test_r,test_c
                        elif visited[test_r][test_c] == min[0]:
                            if test_r < min[1]:
                                min[1], min[2] = test_r, test_c
                            elif test_r == min[1] and test_c < min[2]:
                                min[1], min[2] = test_r, test_c
                    else:
                        queue.append((test_r,test_c))
    return min

def move(row,col,idx):
    visited2 = [[0 for _ in range(N)] for _ in range(N)]
    que = deque()
    que.append((row,col))
    ed_r, ed_c = passenger[idx-1][2] -1 , passenger[idx-1][3] - 1
    while que:
        now_r, now_c = que.popleft()

        # print('now', now_r, now_c)
        # for i in range(N):
        #     print(visited2[i])

        for i in range(4):
            test_r = now_r + drow[i]
            test_c = now_c + dcol[i]
            if (test_r,test_c) == (ed_r, ed_c):
                return visited2[now_r][now_c] + 1, test_r, test_c
            if iswall(test_r,test_c) and visited2[test_r][test_c] == 0:
                if maplist[test_r][test_c] != 1:
                    visited2[test_r][test_c] += visited2[now_r][now_c] + 1
                    que.append((test_r,test_c))
    return -1, row, col

N, M, fuel = map(int, input().split())
maplist = [list(map(int, input().split())) for _ in range(N)]

st_r, st_c = map(int, input().split())
st_r -= 1
st_c -= 1
passenger = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    maplist[passenger[i][0] -1][passenger[i][1] -1] = (i+1)*11

# for i in range(N):
#     print(maplist[i])

for _ in range(M):
    # print('fuel', fuel, 'st', st_r, st_c)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    d, r, c = min_distance(st_r, st_c)
    if d == N*N:
        fuel = -1
        break
    idx = maplist[r][c]//11
    maplist[r][c] = 0
    fuel -= d
    # print(fuel)
    if fuel < 0:
        break
    distance, ed_r, ed_c = move(r,c,idx)
    if distance == -1:
        fuel = -1
        break
    if fuel < distance:
        fuel = -1
        break
    fuel += distance
    # print(fuel)
    M -= 1
    st_r, st_c = ed_r, ed_c

if fuel < 0:
    print(-1)
else:
    print(fuel)