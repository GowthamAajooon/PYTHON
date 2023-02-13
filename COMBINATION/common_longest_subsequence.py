from itertools import combinations
s1 = "ABCDGHE"
s2 = "ACDGHRE"
# CDGH
a1 = []
for i in range(len(s1)):
    a = combinations(s1,i)
    for i in a:
        a1.append(i)
a2 = []
for i in range(len(s2)):
    a = combinations(s2,i)
    for i in a:
        a2.append(i)
ac = list(set(a1+a2))
for i in ac:
    if "CDGH" == "".join(i):
        print("Yes")
        break
else:
    print("No")

    
    @@@@@________doubt
