T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    friends = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)

    ls = []
    for friend in friends[1]:
        ls.append(friend)
        for friend2 in friends[friend]:
            if friend2 != 1:
                ls.append(friend2)

    print("#{} {}".format(tc,len(set(ls))))