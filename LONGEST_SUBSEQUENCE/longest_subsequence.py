#a = [1,2,3,4,9,8,7,6,11,12,13,14,21,22,23,24]
a = [56,4,3,8,7,9]
a = sorted(list(set(a)))
s,k,j=1,[],[]
for i in range(1,len(a)):
    if a[i-1]+1==a[i]:
        s+=1
    else:
        k.append(s)
        s=1
j.append(s)
j = j+k
if j[-2] == j[-1]:
    print(0)
else:
    print(max(j))
