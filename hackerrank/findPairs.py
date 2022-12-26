import sys

n = 10
ar = [1, 2, 1, 3, 4, 2, 5, 6, 4, 3]

ar.sort()
res = 0
temp = 0

for x in range(n):
    if ar[x] != temp:
        temp = ar[x]
        m = int(ar.count(ar[x]))
        res += int(m / 2) if m % 2 == 0 else int((m - 1) / 2 if m > 1 else 0)

#print(res)

for line in sys.stdin:
    str1=line.split(';')[0]
    str2=line.split(';')[1]

    res =""
    str1_ind=0
    str2_ind=0
    ind_res = str2.index(str1[0]) #5

    for i in str1[1:]:
        ind = str2.index(str1[i]) #0
        if ind_res < ind:
            res = res + str1[i+1]
        print(res, end="")
