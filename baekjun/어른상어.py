from _collections import deque

def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

N, M, k = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
now = list(map(int, input().split()))
directions = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

sharks = []
for i in range(N):
    for j in range(N):
        if map_list[i][j] != 0:
            sharks.append((map_list[i][j],i,j))
            map_list[i][j] = [map_list[i][j], k]

sharks.sort(key=lambda x: x[0])
sharks = deque(sharks)

ans = 0
out = []
while ans <= 1000:
    for _ in range(M):
        num, r, c = sharks.popleft()
        if num in out:
            continue
        direction = directions[num-1][now[num-1]-1]
        self_move = []

        for i in direction:
            test_r = r + drow[i-1]
            test_c = c + dcol[i-1]
            if iswall(test_r, test_c):
                if map_list[test_r][test_c] == 0:
                    now[num-1] = i
                    sharks.append((num,test_r,test_c))
                    break
                elif map_list[test_r][test_c][0] == num:
                    self_move.append((num, test_r, test_c, i))
        else:
            num, row, col, idx = self_move.pop(0)
            sharks.append((num, row, col))
            now[num-1] = idx

    for i in range(N):
        for j in range(N):
            if map_list[i][j] != 0:
                if map_list[i][j][1] == 1:
                    map_list[i][j] = 0
                else:
                    map_list[i][j][1] -= 1

    out = []
    for shark in sharks:
        num, row, col = shark
        if map_list[row][col] == 0:
            map_list[row][col] = [num, k]
        elif map_list[row][col][0] == num:
            map_list[row][col] = [num, k]
        else:
            out.append(num)

    M = len(sharks)

    if M == 1:
        break

    ans += 1

if ans > 1000:
    print(-1)
else:
    print(ans)