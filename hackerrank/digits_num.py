"""
Given a number of digits from 0-9 where each digit can appear only once, find the number iteration it
would take to traverse the digits given in num. going from a -> b is one iteration

Example
digit: 0123456789
num: 210

output: 4

Explanation: to reach to 2 you take 2 iterations
to go back to 1 you take 1 iteration
and then to 0 you take 1 iteration
so total 4 iterations

"""
digits = "0123456789"
num = "210"

nl = []
count_num = 0

for n in num[:]:
    nl.append(digits.index(n))

count_num = nl[0]

for c in range(len(nl) - 1):
    count_num += abs(nl[c] - nl[c + 1])

print(count_num)
