# ---------------QUESTION 
# FIND THE POSSIBLE WAY FOR THE GIVEN INPUT
# INPUT : 4
# OUTPUT : 5

# EXPLANATION:
#   [1, 1, 1, 1]
#   [1, 1, 2]
#   [1, 3]
#   [2, 2]
#   [4]
  
# ____________________________________________________  
from itertools import product
n = int(input())
l =[i for i in range(1,n+1)]
h,h1 = [],[]
for j in range(1,len(l)+1):
    for i in product(l,repeat=j):
        if sum(i)==n:
            h.append(sorted(list(i)))
for i in h:
    if i not in h1:
        h1.append(i)
print(len(h1))

# INSTRUCTIONS TO USE IN A OPTIMIZED WAY
# PACKAGE
# ---------[   itertools -> product   ]

# usage all possible way in a list 
# synatx:
# for i in product('list',repeat='count'):
#   print(sorted(list(i)))
  
# _____________________________________________________
# ATERNATIVE METHOD:

import itertools
print(len([sorted(list(j)) for i in range(1,int(input())+1) for j in itertools.combinations_with_replacement([1,2,3,4],i) if sum(j)==n ]))
print(len(k))


# PACKAGE
# ---------[   itertools -> itertools.combinations_with_replacement   ]

# usage all possible way in a list
# syntax:
# for j in itertools.combinations_with_replacement('list','count')
#   print(sorted(list(j)))

