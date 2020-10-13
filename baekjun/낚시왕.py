drow = [-1, 1, 0, 0]
dcol = [0, 0, 1, -1]

R,C,M = map(int, input().split())
maplist = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    maplist[r-1][c-1] = [s,d,z]

for i in range(R):
    print(maplist[i])