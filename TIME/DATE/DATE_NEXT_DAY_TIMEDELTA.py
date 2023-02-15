import datetime
from datetime import timedelta 
y = input()
y = y.split("/")
g = datetime.datetime(int(y[2]), int(y[1]), int(y[0])) 
d= g + timedelta(days = 1) 
d = str(d)
d = d[:11].split("-")
print(str(int(d[2]))+"/"+str(int(d[1]))+"/"+str(int(d[0])))
