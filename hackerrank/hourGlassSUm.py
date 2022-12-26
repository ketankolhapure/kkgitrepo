"""
Given a  2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g

There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

Example


-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0

 The  hourglass sums are:
 -63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18

The highest hourglass sum is  from the hourglass beginning at row 1, column 2:
0 4 3
  1
8 6 6

Function Description

Complete the function hourglassSum in the editor below.

hourglassSum has the following parameter(s):

int arr[6][6]: an array of integers
Returns

int: the maximum hourglass sum
Input Format

Each of the  lines of inputs  contains  space-separated integers .

Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19
"""

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