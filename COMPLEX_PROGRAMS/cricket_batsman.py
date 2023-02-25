#CRICKET BATSMAN


n = input()
bat1,bat2,bow,f,r=0,0,0,0,0
if len(n)==6:
    for i in n:
        if i=='Y':
            bow+=1  
        elif i=='.':
            bow+=0
        elif i.isnumeric()==True:
                j = int(i)
                if j%2==0 and f==0:
                    bat1+=j
                elif j%2==1 and f==0:
                    bat1+=j
                    f=1
                elif j%2==0 and f==1:
                    bat2+=j
                elif j%2==1 and f==1:
                    bat2+=j
                    f=0
        else:
            r = 1
    if r==0:
        print(f"BATSMAN 1: {bat1}\nBATSMAN 2: {bat2}\nBOWLER: {bat1+bat2+bow}")
    else:
        print("Invalid")
    
    
else:
    print("Invalid")
