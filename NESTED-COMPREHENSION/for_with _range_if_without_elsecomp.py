print(*[i for i in range(1,int(input())+1) if i%5!=0 and i%7!=0 ])


n = int(input())
print(*[i for i in range(n//2,((n//2)+1)*-1,-1) if i!=0])
