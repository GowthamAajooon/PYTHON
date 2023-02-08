n = input()
lb=[]
k = []
for i in n:
    if i=="(":
        lb.append(i)
    if i==")":
        lb.pop(0)
    k.append(len(lb))
if len(lb)==0:
    print(max(k))
else:
    print("Not a balanced parenthesis")
