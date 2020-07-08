from collections import deque

drow = [1,1,1,0,0,0,-1,-1,-1]
dcol = [-1,0,1,-1,0,1,-1,0,1]

def move_close(row,col):
    global visited

    r, c = now[0]
    if r < row:
        test_r = row - 1
    elif r > row:
        test_r = row + 1
    else:
        test_r = row

    if c < col:
        test_c = col - 1
    elif c > col:
        test_c = col + 1
    else:
        test_c = col

    if visited[test_r][test_c] == 0:
        visited[test_r][test_c] = 1

        if map_list[test_r][test_c] == 'I':
            return -1
        else:
            map_list[test_r][test_c] = 'R'
            temp.append((test_r, test_c))
    else:
        if (test_r, test_c) in temp:
            temp.remove((test_r,test_c))
        map_list[test_r][test_c] = '.'

R, C = map(int, input().split())
map_list = [list(input()) for _ in range(R)]
direction = list(input())
now = []
aduino = deque()

for r in range(R):
    for c in range(C):
        if map_list[r][c] == 'I':
            now.append((r,c))
        if map_list[r][c] == 'R':
            aduino.append((r,c))

cnt = 0
end = False
for dir in direction:
    if end == True:
        break
    cnt += 1
    r, c = now.pop()
    map_list[r][c] = '.'
    r += drow[int(dir)-1]
    c += dcol[int(dir)-1]
    if map_list[r][c] == 'R':
        end = True
        break
    else:
        map_list[r][c] = 'I'
        now.append((r,c))

    visited = [[0 for _ in range(C)] for _ in range(R)]
    temp = []
    for _ in range(len(aduino)):
        row,col = aduino.popleft()
        map_list[row][col] = '.'
        if move_close(row,col) == -1:
            end = True
            break

    aduino = deque(temp)

if end == True:
    print('kraj', cnt)
else:

    while aduino:
        r, c = aduino.popleft()
        map_list[r][c] = 'R'

    for i in range(R):
        print(*map_list[i], sep='')