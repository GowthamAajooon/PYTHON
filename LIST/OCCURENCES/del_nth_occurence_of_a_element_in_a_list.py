line = "Hello What do you think? Hello here we come"
n = 2
word = "Hello"
c=0
for i in range(0,len(line)-1):
    if line[i]==word:
        c+=1
        if c==n:
            del line[i]
print(line)
