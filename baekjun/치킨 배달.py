from collections import deque
from itertools import combinations

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
candidate = []
homes = []
mn = N**N

for row in range(N):
    for col in range(N):
        if city[row][col] == 2:
            candidate.append((row,col))
        if city[row][col] == 1:
            homes.append((row,col))

combi = list(combinations(candidate,M))
for c in combi:
    d = [N ** 2] * len(homes)
    for i in range(len(homes)):
        for j in range(M):
            row, col = c[j][0], c[j][1]
            if d[i] > abs(row - homes[i][0]) + abs(col - homes[i][1]):
                d[i] = abs(row - homes[i][0]) + abs(col - homes[i][1])
    if mn > sum(d):
        mn = sum(d)

print(mn)