a = [
    [1,-2,3,4,5,6],
    [2,3,-4,5,-6,7],
    [3,4,-5,6,-7,8],
    [4,5,-6,-7,8,-9],
    [5,-6,7,-8,9,0],
    [6,7,8,9,-0,1],
]

result = []
for j in range(1, 5):
    for i in range(1, 5):
        result.append(a[j][i] + a[j-1][i] + a[j-1][i-1] + a[j-1][i+1] + a[j+1][i] + a[j+1][i-1] + a[j+1][i+1])

print(max(result))