import math

def init(node,start,end):
    if start == end:
        tree[node] = num[start]
        return tree[node]
    else:
        mid = (start+end)//2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
        return tree[node]

def update(node,start,end,target,diff):
    if target < start or target > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, target, diff)
        update(node*2+1, mid+1, end, target, diff)

def subsum(node,start,end,left,right):
    if left > end or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        return subsum(node*2, start, mid, left, right) + subsum(node*2+1, mid+1, end, left,right)

N, M, K = map(int, input().split())
num = []
for _ in range(N):
    num.append(int(input()))

h = math.ceil(math.log(N,2) + 1)
tree = [0] * (2**h -1)
init(1,0,N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        diff = c - num[b-1]
        num[b-1] = c
        update(1,0,N-1,b-1,diff)
    elif a == 2:
        print(subsum(1,0,N-1,b-1,c-1))