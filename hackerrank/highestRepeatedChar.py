"""
Given a string s, return the most frequent char (an alphabet letter) in the string s

example
input: s = "abcddefda111122222222"
output: d
"""


def checkhighestchar(s):
    hchar = ''
    tempchar = ''
    tempcount = 0
    t = list(s)

    t.sort()

    for i in t[:]:
        if i.isalpha():
            if tempchar != i:
                tempchar = i
            if s.count(tempchar) > tempcount:
                tempcount = s.count(tempchar)
                hchar = tempchar

    return hchar


s = 'AAabcddefda111122222222'

print(checkhighestchar(s))
