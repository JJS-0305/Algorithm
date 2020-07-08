A, B, x, y, p, q = map(int, input().split())

holes = [(A,0), (0,B), (0,0), (A,B)]

A-x, A, A, A, A, A,
B-y, B, B, B, B, B,


# cnt = 0
# first = (x,y)
# while (x,y) not in holes:
#     x += p
#     y += q
#     if x == 0 or x == A:
#         p = -p
#         cnt += 1
#
#     elif y == 0 or y == B:
#         q = -q
#         cnt += 1
#
#     if (x,y) == first:
#         cnt = -1
#         break
print(cnt)