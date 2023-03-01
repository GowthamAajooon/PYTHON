for i in range(int(input())):
    l = list(map(int,input().split()))
    m = list(map(str,input().split()))[:l[1]]
    s,c = [],[]
    for i in m:
        f = []
        for j in i:
            p = str(ord(j))[-1]
            if int(p)%2!=0:
                f.append(1)
            else: 
                f.append(0)
        s.append(f)
for i in s:
    h = 1
    for j in i:
        h = h*j
    c.append(h)
print("EVEN" if sum(c)%2==0 else "ODD")



'''

1
2 2
abc abcd           even

	Input	Expected	Got	
1
2 2
abc abcd
EVEN
EVEN
1
2 3
azbde abcher acegk
ODD
ODD
1
4 3
everyonehieveryonehello sample javaprogrammingpythonprogramming
EVEN
EVEN


'''
