def checkt(t):
    return 1 <= t <= 10


def checkgift(g, n):
    return (1 <= g <= 100000) and (1 <= n <= g)


def checkprice(p):
    if (0<= int(p) <=10000000):
        return int(p)
    else:
        exit


T = int(input())

R = []

if checkt(int(T)):
    for t in range(T):
        N = int(input())
        G = int(input())
        P = input()
        buy = 0
        if checkgift(G, N):
            P_list = [checkprice(p) for p in list(P.split(" "))]
            P_list.sort()
            for n in range(N):
                buy += P_list[n]
            R.append(buy)
    for n in range(len(R)):
        print(R[n])

