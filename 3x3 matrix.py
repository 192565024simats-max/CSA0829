A=[[1,1,1],[2,2,2],[3,3,3]]
B=[[1,1,1],[2,2,2],[3,3,3]]
C=[[1,1,1],[2,2,2],[3,3,3]]
AB= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            AB[i][j]+=A[i][k]*B[k][j]

ABC= [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            ABC[i][j]+=AB[i][k]*C[k][j]

for row in ABC:
    print(row)            
