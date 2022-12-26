import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
def checkLimit(n):
    return 1 <= n <= 1300

n = int(input())
n_ary = []

if checkLimit(n):
    for i in range(1955):
        if str(i).find('2') == -1 and str(i).find('14') == -1:
            n_ary.append(i)

print(n_ary[n])
