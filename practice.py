import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

checkboard = [[0]* 19 for _ in range(19)]

for i in range(19):
    for j in range(19):
        if(j!=18):
            checkboard[i][j] = list(map(int, sys.stdin.readline().split()))
        elif(j==18):
            checkboard[i][j] = map(int, sys.stdin.readline())
n=int(sys.stdin.readline())
for i in range(n):
    xx,yy=list(map(int, sys.stdin.readline().split()))
    for j in range(19):
        if(checkboard[xx][j]==0):
            checkboard[xx][j]=1
        else:
            checkboard[xx][j]=0
    for k in range(19):
        if(checkboard[k][yy]==0):
            checkboard[k][yy]=1
        else:
            checkboard[k][yy]=0

for i in range(19):
    for j in range(19):
        if(j!=18):
            print(checkboard[i][j], end=" ")
        if(j==18):
            print(checkboard[i][j])

