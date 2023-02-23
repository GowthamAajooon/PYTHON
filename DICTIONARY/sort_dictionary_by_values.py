d = "Tye a yuiv seeing thee sets".split()
p = [len(i) for i in d]
f = dict(zip(d,p))
f = dict(sorted(f.items(), key=lambda x: x[1]))
print(*list(f.keys()))
