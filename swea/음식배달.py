from _collections import deque
from itertools import combinations

def solve(k):
    if k == len(food):
        pass
    else:
        pass

T = int(input())
for tc in range(T):
    N = int(input())
    maplist = [[] for _ in range(N)]
    for i in range(N):
        maplist[i] = list(map(int, input().split()))

    home, food = [], []
    for r in range(N):
        for c in range(N):
            if maplist[r][c] == 1:
                home.append((r,c))
            elif maplist[r][c] > 1:
                food.append((r,c,maplist[r][c]))
