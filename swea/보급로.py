from collections import deque

def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def dijkstra():
    queue = deque()
    cost[0][0] = 0
    queue.append((0,0))

    while queue:
        r,c = queue.popleft()
        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r,test_c):
                temp = cost[r][c] + map_list[test_r][test_c]

                if cost[test_r][test_c] >= 0:
                    if temp < cost[test_r][test_c]:
                        cost[test_r][test_c] = temp
                        queue.append((test_r,test_c))
                else:
                    cost[test_r][test_c] = temp
                    queue.append((test_r, test_c))


drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    map_list = [list(map(int,input())) for _ in range(N)]
    cost = [[-1 for _ in range(N)] for _ in range(N)]
    dijkstra()
    print("#{} {}".format(tc,cost[N-1][N-1]))