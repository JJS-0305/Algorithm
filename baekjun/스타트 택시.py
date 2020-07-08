from collections import deque

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

# 벽인지 체크
def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

# 출발점에서 제일 가까운 승객 찾기
def close_distance(row, col):
    global k

    for idx in range(M):
        # 출발지점에 승객이 있는 경우
        if (row-1, col-1) == passenger[idx]:
            move(idx)  # 승객을 태우고 도착지로 이동하는 함수 실행
            next_row, next_col = destination[idx]  # 다음 출발지로 이번 도착지를 할당
            # 이미 태우고 도착지로 데려다 준 승객의 출발,도착 정보는 (-1,-1)로 바꿈
            passenger[idx] = (-1, -1)
            destination[idx] = (-1, -1)
            return next_row + 1, next_col + 1

    # 방문 체크
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[row - 1][col - 1] = 1

    queue = deque()
    queue.append((row-1, col-1))

    chk = N*N   # 출발점에서 거리가 같은 지점을 체크하기 위해 임의로 N*N을 배정
    memo = []   # 거리가 같은 승객의 index 번호를 모음
    while queue:
        r, c = queue.popleft()
        # 거리가 같은 지점이 모두 끝나면 if문 실행
        # chk = 출발점부터의 거리

        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r, test_c) and visited[r][c] <= chk:
                # 방문한 적 없고 벽이 아닌지 체크
                if visited[test_r][test_c] == 0 and maplist[test_r][test_c] != 1:
                    visited[test_r][test_c] = visited[r][c] + 1
                    queue.append((test_r, test_c))
                    for j in range(len(passenger)):
                        # 승객의 출발 정보와 같은지 확인
                        if passenger[j] == (test_r, test_c):
                            # chk에 가장 가까운 거리 할당
                            chk = visited[r][c]
                            memo.append(j)          # memo리스트에 승객의 index 추가


    if memo:
        k -= chk
        memo.sort(key=lambda x: passenger[x])
        idx = memo[0]
        move(idx)  # 승객을 태우고 도착지로 이동하는 함수 실행
        next_row, next_col = destination[idx]  # 다음 출발지로 이번 도착지를 할당
        # 이미 태우고 도착지로 데려다 준 승객의 출발,도착 정보는 (-1,-1)로 바꿈
        passenger[idx] = (-1, -1)
        destination[idx] = (-1, -1)
        return next_row + 1, next_col + 1

    return -1, -1       # 승객을 만나지 못하면 (-1, -1) 반환. ex) 벽에 가로 막힘.

def move(n):
    global k

    visited2 = [[0 for _ in range(N)] for _ in range(N)]
    visited2[passenger[n][0]][passenger[n][1]] = 1          # passenger[idx]에는 승객의 행,열 번호 할당
    que = deque()
    que.append(passenger[n])

    while que:
        r, c = que.popleft()
        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r, test_c):
                if visited2[test_r][test_c] == 0 and maplist[test_r][test_c] != 1:
                    visited2[test_r][test_c] = visited2[r][c] + 1
                    que.append((test_r, test_c))
                    # 이동 경로가 승객의 도착지점인지 확인
                    if destination[n] == (test_r, test_c):
                        # 남은 연료량이 이동하는데 소모하는 연료량보다 같거나 많은지 체크!
                        if k >= visited2[r][c]:
                            k += visited2[r][c]
                        # 남은 연료량으로 도착지까지 가지 못한다면 k = -1 할당
                        else:
                            k = -1
                        return


N, M, k = map(int, input().split())
maplist = [list(map(int, input().split())) for _ in range(N)]
st_row, st_col = map(int, input().split())
passenger = []
destination = []

for _ in range(M):
    st_r, st_c, ed_r, ed_c = map(int, input().split())
    passenger.append((st_r - 1, st_c - 1))
    destination.append((ed_r - 1, ed_c - 1))

# 승객의 수 만큼 반복
for _ in range(M):
    # 처음 택시 좌표 이후 승객의 도착지를 출발지로 재설정
    st_row, st_col = close_distance(st_row, st_col)

    # 승객을 만나지 못한 경우 k = -1 로 변경
    if (st_row, st_col) == (-1, -1):
        k = -1
        break
    # 연료가 다 떨어져서 승객을 태우고 이동하지 못한 경우 k = -1 할당
    if k < 0:
        k = -1
        break

print(k)
