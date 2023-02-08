n = int(input())
d = {}
while len(d)<n:
    name = input()
    age = int(input())
    if name not in d:
        d[name] = age
        
n1,a=[],[]
for k,v in d.items():
    n1.append(k)
    a.append(v)
print(n1)
print(a)
