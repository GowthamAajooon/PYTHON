def largestHistogram(lst):
    largestArea=0;
    
    for i in range(len(lst)):
        area=lst[i]
        for j in range(i-1,-1,-1):
            if(lst[j]<lst[i]):break;
            area+=lst[i];
        for j in range(i+1,len(lst)):
            if(lst[j]<lst[i]):break;
            area+=lst[i]
        largestArea=max(largestArea,area)
        
    return largestArea

lst = [[1,0,1,1],
       [0,0,1,1],
       [1,1,1,1],
       [1,1,0,0]]
a = []
histList=[]

for i in range(len(lst)):
    if(i==0):histList=lst[0].copy()
    else:
        for j in range(0,len(lst[i])):
            if(lst[i][j]==0): histList[j]=0
            else: histList[j]=histList[j]+1
    a.append(largestHistogram(histList))
print(a)
