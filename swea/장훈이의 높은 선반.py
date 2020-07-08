def powerset(n, k, tot):
    global mn
    if tot >= B:
        if tot < mn:
            mn = tot
        return
    elif n > k:
        A[k] = 1
        powerset(n, k + 1, tot + H[k])
        A[k] = 0
        powerset(n, k + 1, tot)


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0 for _ in range(N)]

    mn = N * B
    powerset(N, 0, 0)
    print("#{} {}".format(tc, mn - B))