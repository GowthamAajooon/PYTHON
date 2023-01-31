def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs

p=combs([1,2,3,4,5])
for i in p:
    print(i)
