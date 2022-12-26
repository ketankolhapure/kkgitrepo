stq = input()

a = stq.split(' ')
s = int(a[0])
t = int(a[1])
q = int(a[2])

def checkLimit(n, l, h):
    return l <= n <= 10**h

t_ary = set()
q_ary = set()

if checkLimit(s, 1, 9):
    if checkLimit(t, 0, 6):
        if checkLimit(q, 0, 6):
            for x in range(t):
                t_ary.add(int(input()))

            for y in range(q):
                q_ary.add(int(input()))

            res = t_ary.intersection(q_ary)

            for i in q_ary:
                if i in res:
                    print('N')
                else:
                    print('Y')

