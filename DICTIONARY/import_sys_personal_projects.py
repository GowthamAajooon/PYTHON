import sys
h=sys.stdin.readlines()

k=[]
for i in range(1,len(h)-1):
    k.append(h[i].replace("{","").replace("}","").replace(",","").replace("id: ","").replace("parentId: ","").replace("name: ","").replace("'","").split())
a,b,c=[],[],[]
for i in k:
    a.append(i[0])
    b.append(i[1])
    c.append(i[2])
id1,pid = {},{}
for i in range(len(k)):
    id1[a[i]],pid[a[i]]  = b[i],c[i]

if "0" in b:
    print("labels = [")
    output=""
    for k,v in pid.items():
        print("    '",end="")
        o=v
        while(id1[k]!="0"):
            pvl=pid[id1[k]]
            o=pvl+"/"+o
            k=id1[k]
        print(o,end="',\n")
    print("]")
else:
    print("Error. No root found")

    '''
folders  = [
{id: 27, parentId: 15, name: 'projects'},
{id: 81, parentId: 27, name: 'novel'},
{id: 15, parentId: 0, name: 'personal'},
{id: 35, parentId: 27, name: 'blog'},
]
'''
'''
import sys
msg=sys.stdin.readlines()
print(msg)

'''

m = dict()
h = []

while m!="]":
    m = input()
    h.append(m)
    
k=[]
for i in range(1,len(h)-1):
    k.append(h[i].replace("{","").replace("}","").replace(",","").replace("id: ","").replace("parentId: ","").replace("name: ","").replace("'","").split())
a,b,c=[],[],[]
for i in k:
    a.append(i[0])
    b.append(i[1])
    c.append(i[2])
id1,pid = {},{}
for i in range(len(k)):
    id1[a[i]],pid[a[i]]  = b[i],c[i]


print("label = [")
output=""
for k,v in pid.items():
    print("    '",end="")
    output=v
    while(id1[k]!="0"):
        parentval=pid[id1[k]]
        output=parentval+"/"+output
        k=id1[k]
    print(output,end="'\n")
print("]")
