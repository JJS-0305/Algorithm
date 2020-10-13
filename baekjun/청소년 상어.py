from copy import deepcopy

dcol = [0,-1,-1,-1,0,1,1,1]
drow = [-1,-1,0,1,1,1,0,-1]

def iswall(row,col):
    if row < 0 or row >= 4:
        return False
    if col < 0 or col >= 4:
        return False
    return True

def dfs(row,col,dir,ls,fish):
    cnt = 0
    n = ls[row][col]
    ls[row][col] = 0
    shark = fish[n]
    fish[n] = 0
    cnt += n
    ls2, fish2 = move_fish(ls,fish,shark)

    # for i in range(4):
    #     print(ls2[i])
    # print('fish', fish2)
    # print()

    mx = 0
    for i in range(1,4):
        change_r = row + drow[dir-1]*i
        change_c = col + dcol[dir-1]*i
        if iswall(change_r,change_c) and ls2[change_r][change_c]:
            # print('go',n,i,'change',change_r,change_c)
            candidate = dfs(change_r,change_c,fish[ls2[change_r][change_c]][2],deepcopy(ls2),deepcopy(fish2))
            if candidate > mx:
                mx = candidate

    cnt += mx

    return cnt

def move_fish(ls,fish,shark):
    for i in range(1,17):
        if fish[i]:
            r,c,dir = fish[i]
            dir -= 1
            move = False
            while not move:
                move_r = r + drow[dir]
                move_c = c + dcol[dir]
                if iswall(move_r,move_c) and (move_r, move_c) != (shark[0],shark[1]):
                    if ls[move_r][move_c]:
                        change = ls[move_r][move_c]
                        ls[move_r][move_c], ls[r][c] = i, change
                        fish[i] = [move_r,move_c,dir+1]
                        fish[change][0], fish[change][1] = r,c
                    else:
                        n = ls[r][c]
                        ls[move_r][move_c] = n
                        ls[r][c] = 0
                        fish[i] = [move_r,move_c,dir+1]
                    move = True
                else:
                    dir = (dir + 1) % 8

    return ls,fish

maplist = [[0 for _ in range(4)] for _ in range(4)]
fish = [0 for _ in range(17)]

for r in range(4):
    data = list(map(int, input().split()))
    for c in range(4):
        num = data[2*c]
        maplist[r][c] = num
        fish[num] = [r,c,data[2*c+1]]

ans = dfs(0,0,fish[maplist[0][0]][2], maplist,fish)
print(ans)