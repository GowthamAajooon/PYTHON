r = "hello there"
tr = "e"
k = 3
p = -1
for i in range(0,k): #use r.count(tr) instead of k
    p = r.find(tr,p+len(tr),len(r))
print(p)
