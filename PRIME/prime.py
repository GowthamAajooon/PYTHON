n = int(input())
m = int(input())
for dank in range(n,m+1):
    if (dank>1):
        for i in range(2,dank):
            if(dank%i)==0:
                break
        else:
            print(dank)
