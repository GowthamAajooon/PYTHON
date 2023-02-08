m1 = " {Mohan, Kumar}, {Gram, Teresa}, {plum, Green}, {Kumar, Kishan}, {Teresa, Param}, {Green, Camaroon}"
t = "Gram"
a = []
m1 = m1.replace("},","}").replace(", ",",").split()
for i in m1:
    a.append(i.replace("{","").replace("}","").replace(","," ").split())
print(a)
for i in a:
    if i[0]==t:
        k = i[1]
        for i in a:
            if k==i[0]:
                print(i[1])
