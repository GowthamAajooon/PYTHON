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
