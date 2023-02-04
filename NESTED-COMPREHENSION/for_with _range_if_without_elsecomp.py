print(*[i for i in range(1,int(input())+1) if i%5!=0 and i%7!=0 ])


n = int(input())
print(*[i for i in range(n//2,((n//2)+1)*-1,-1) if i!=0])


n = int(input())
l = list(map(int,input().split()))
print(sum([i for i in l if i>0]))


n = int(input())
l = list(map(int,input().split()))
print(sum([i for i in l if i%2!=0]))


n1,n2 = int(input()),int(input())
m1,m2=n1,n2
if n1>0 and n2>0:
    if n1==n2:
        m = [[int(input()) for i in range(n1)] for j in range(n2)]
        print("Primary diagonal elements:")
        for i in range(n1):
            for j in range(n2):
                if i == j:
                    print(m[i][j])
        print("Secondary diagonal elements:")  
        for i in range(m1):
            for j in range(m2):
                if i+j == m1-1:
                    print(m[i][j])
    else:
        print("Row and column size should be same")
else:
    print("Row and column size should not be negative")
    
