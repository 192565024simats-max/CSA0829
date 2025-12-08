A = [[1, 1],
     [2, 2]]

B = [[1, 1],
     [2, 2]]

AB= [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            AB[i][j]+=A[i][k]*B[k][j]

for row in AB:
    print(row)
