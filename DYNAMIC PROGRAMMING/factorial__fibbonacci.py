# DYNAMIC PROGRAMMING
# =============================================================================
# FACTORIAL
# =============================================================================
e = [int(input()) for  i in range(int(input()))]
f = [0 for i in range(max(e)+1)]
f[0],f[1]=1,1
for i in range(2,max(e)+1):
    f[i] = i*f[i-1] 
for i in e:
    print(f[i-1])

    
   
# =============================================================================
# FIBONACCI
# =============================================================================
e =[int(input()) for i in range(int(input()))]
f = [-1 for i in range(max(e)+1)]
f[0],f[1]=0,1
for i in range(2,max(e)+1):
    f[i]=f[i-1]+f[i-2]
for i in e:
    print(f[i])

