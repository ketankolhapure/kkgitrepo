s = "{}[]()"
l = []

for i in s[:]:
    l.append(i)

if l.count('{') == l.count('}') and l.count('[') == l.count(']') and l.count('{') == l.count('}'):
    print(True)


def isValid(s):
    stack = []
    D = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in D.values():
            stack.append(char)
        else:
            if stack == [] or stack.pop() != D[char]:
                return False
    return stack == []

print(isValid(s))