n,c =[i for i in map(int,str(input()))],0
for i in range(len(n)-2):
    if (n[i]==n[i+1]-1==n[i+2]-2) or (n[i]-2==n[i+1]-1==n[i+2]):
        c+=1
if c>=1:
    print("Yes")
else:
    print("No")
    
    
    Note: ipo genral la consecutive kandu pudika sonna len-1 
          ila 3 consecutive keta 
          n = 3
      range = len-(n-1)
      ipdi irukanum
