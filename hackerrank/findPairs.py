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

print(res)

"""
Another solution using dictionary
dictnum = {}

al = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1]

for i in al:
    dictnum[i] = al.count(i)

result = 0

for i in dictnum.keys():
    if dictnum[i] > 1:
        if dictnum[i] % 2 == 0:
            result += dictnum[i] / 2
        else:
            result += (dictnum[i] - 1) / 2

print(result)
"""

