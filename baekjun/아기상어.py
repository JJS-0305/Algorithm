from collections import deque

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def iswall(row,col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def find_fish(row,col,shark_size):
    queue = deque()
    queue.append((row,col))
    visited = [[0 for _ in range(N)] for _ in range(N)]

    min = [N*N, -1, -1]
    while queue:
        r, c = queue.popleft()
        if visited[r][c] > min[0]:
            return min
        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r, test_c):
                if maplist[test_r][test_c] <= shark_size and visited[test_r][test_c] == 0 and maplist[test_r][test_c] != 9:
                    visited[test_r][test_c] = visited[r][c] + 1
                    queue.append((test_r,test_c))
                    if 0 < maplist[test_r][test_c] < shark_size:
                        if min[0] > visited[test_r][test_c]:
                            min[0], min[1], min[2] = visited[test_r][test_c], test_r, test_c
                        elif min[0] == visited[test_r][test_c]:
                            if min[1] > test_r:
                                min[1], min[2] = test_r, test_c
                            elif min[1] == test_r and min[2] > test_c:
                                min[1], min[2] = test_r, test_c
    return min

N = int(input())

maplist = [list(map(int, input().split())) for _ in range(N)]

shark_size = 2
shark_r, shark_c = -1, -1
fish = [0 for _ in range(7)]
cnt = 0
time = 0

for row in range(N):
    for col in range(N):
        if maplist[row][col] == 9:
            shark_r, shark_c = row, col
        elif maplist[row][col] != 0:
            fish[maplist[row][col]] += 1
t = 0
while t < N*N:
    # print('shark', shark_r, shark_c,'size', shark_size, 'cnt', cnt)
    # for i in range(N):
    #     print(maplist[i])
    # print()
    t,r,c = find_fish(shark_r, shark_c, shark_size)
    maplist[shark_r][shark_c] = 0
    if t == N*N:
        break
    else:
        time += t
        fish[maplist[r][c]] -= 1
        shark_r, shark_c = r, c
        maplist[r][c] = 9
        cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0

    if sum(fish[:shark_size]) == 0:
        break

print(time)