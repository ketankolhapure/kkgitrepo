"""
+ new score add previous 2 scores
D 2 * previous score
C remove previous score
[5 2 c d +]
"""

def checkOps(ops):
    return True if 1 <= len(ops) <= 1000 else False

def calPoints(ops) -> int:
    if checkOps(ops):
        score = []

        for i in range(0, len(ops)):
            if '-' in ops[i]:
                score.append(int(ops[i]))
            elif ops[i].isnumeric():
                score.append(int(ops[i]))
            elif ops[i] == "C":
                score.pop()
            elif ops[i] == "D":
                score.append(score[-1] * 2)
            elif ops[i] == "+":
                score.append(score[-1] + score[-2])

        result = sum(score)
        return result

ops = ["5", "2", "C", "D", "+"]
print(calPoints(ops))

