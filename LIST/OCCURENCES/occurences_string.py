a ="aabbbaabba"
h = [idx for idx,val in enumerate(a) if 'a' == val]
print(*h)
