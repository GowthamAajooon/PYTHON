def fill(i,j,box,res):
    if (i>=0 and i<len(box)) and (j>=0 and j<len(box)) and box[i][j]=='0' and res[i][j]=='0' and res[i][j]!='1':
        res[i][j]='1'
        fill(i+1,j,box,res)
        fill(i-1,j,box,res)
        fill(i,j+1,box,res)
        fill(i,j-1,box,res)

n = "[[1,1,1,1,1,1,1,0],[1,0,0,1,0,1,1,0],[1,0,1,1,0,1,1,0],[1,0,0,1,0,1,0,1],[1,1,1,1,1,1,1,0]]"
n = n.split("],[")
box = []
for i in n:
    box.append( i.replace("[[","").replace("]]","").split(",") )
l1 = len(box)
l2 = len(box[0])
# print(l1,l2)
res = [["0" for i in range(l2)]for j in range(l1)]

print("\n".join(" ".join(map(str,i))for i in box))
print()
print("\n".join(" ".join(map(str,i))for i in res))
print()
c = 0
for i in range(1,l1-1):
    for j in range(1,l2-1):
        if box[i][j] == '0' and res[i][j]=='0' and box[i-1][j]=='1' and box[i][j-1]=='1': 
            c+=1
            fill(i,j,box,res)
print(c)
            
#output : 2
