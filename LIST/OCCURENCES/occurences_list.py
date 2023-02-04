a =[11,1,1,1,2,3,3,4,4,3,3,2,2,2,1,1,1,2]
h = [idx for idx,val in enumerate(a) if 2==val]
print(*h)
