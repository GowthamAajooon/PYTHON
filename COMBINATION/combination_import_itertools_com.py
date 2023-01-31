from itertools import combinations
p = [2,3,4,6,7]
p=[[i for i in combinations(p,j)]for j in range(len(p)+1)]
for i in p:
    for j in i:
        if sum(j)==7:
            print(j)


