a ="aabbbaabba"
h = [idx for idx,val in enumerate(a) if 'a' == val]
print(*h)


'''
from collections import Counter
n = input()
s =''
for k,v in Counter(n).items():
    s+=str(k)+str(v)
print(s)
    
'''
n = input()
m = list(set(n))
m.sort()
k = []
for i in range(len(m)):
    k.append(n.count(m[i]))
s =''
for i in range(len(m)):
    s+=m[i]
    s+=str(k[i])
print(s)

