n1,m1 = list(map(int,input().split())),list(map(int,input().split()))
if n1[0]>0 and n1[1]>0 and m1[0]>0 and m1[1]>0:
    if (n1[0]==n1[1]) and (m1[0]==m1[1]):
        mx1 = [list(map(int,input().split())) for i in range(n1[0])]
        mx2 = [list(map(int,input().split())) for i in range(n1[1])]
        print("Addition:")
        for i in range(len(mx1)):
            for j in range(len(mx2)):
                print(mx1[i][j]+mx2[i][j])
        print("Subtraction:")
        for i in range(len(mx1)):
            for j in range(len(mx2)):
                print(mx1[i][j]-mx2[i][j])
    else:
        print("Row and column size should be same for 2 matrices")

else:
    print("Row and column size should not be negative")
