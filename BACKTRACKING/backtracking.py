def check(res,i,j):
    global board
    global pos
    if i==n-1 and j==m-1:
        res[i][j]=1
        tem=[]
        for i in res:
            t=[]
            for j in i:
                t.append(j)
            tem.append(t)
        pos.append(tem)
        return
    if (i>=0 and i<n)  and (j>=0 and j<m) and board[i][j]==0 and res[i][j]!=1:
        res[i][j]=1
        check(res,i+1,j)
        check(res,i,j+1)
        check(res,i,j-1)
        check(res,i-1,j)
        res[i][j]=0
        return
    return

# n=5
# m=5
# board=[
#     [0,0,1,1,1],
#     [1,0,1,1,0],
#     [0,0,0,0,1],
#     [0,1,1,0,0],
#     [0,1,0,1,0]
# ]

# n=10
# m=10
# board=[
#     [0,1,0,0,0,1,0,0,0,1],
#     [0,1,0,1,0,1,0,1,0,1],
#     [0,0,0,1,0,0,0,1,0,0],
#     [1,0,1,0,1,0,1,0,1,0],
#     [1,0,1,1,0,0,1,0,0,0],
#     [0,0,0,0,1,0,1,0,1,1],
#     [0,1,0,1,1,0,1,0,1,0],
#     [1,0,0,0,1,0,0,0,1,1],
#     [1,0,1,0,0,0,1,0,0,1],
#     [0,0,1,0,1,0,0,0,0,0]
# ]

# n=5
# m=5
# board=[
#     [0,1,0,0,0],
#     [0,0,0,1,0],
#     [0,1,1,0,0],
#     [0,1,1,0,1],
#     [1,1,1,0,0]
# ]

n=5
m=5
board=[
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0]
]

print("Given board..")
for i in range(n):
    for j in range(m):
        print(board[i][j],end=" ")
    print()
print()
pos=[]
c=n*m
res=[[0 for j in range(m)] for i in range(n)]
check(res,0,0)
ind=0

if len(pos)==0:
    print("No Possible Solutions")
else:
    print("No. of solutions :",len(pos))
    print("\nPossible solutions are..")
    for i in range(len(pos)):
        s = 0
        for j in range(len(pos[i])):
            for k in range(len(pos[i][j])):
                print(pos[i][j][k],end=' ')
                if pos[i][j][k] == 1:
                    s += 1
            print()
        print('length of above path :',s)
        if s < c:
            ind = i
            c = s
        print("----------------------------")
    res=pos[ind]
    print("Mimimum path")
    for i in res:
        for j in i:
            print(j,end=' ')
        print()
