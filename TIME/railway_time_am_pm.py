from datetime import datetime
n = '10:55:16 pm'
t = datetime.strptime(n,'%I:%M:%S %p')
a = t.strftime('%H:%M:%S')
print(a)
# 22:55:16
from datetime import datetime
n = '12:36:4 pm'
t = datetime.strptime(n,'%I:%M:%S %p')
a = t.strftime('%H:%M:%S')
print(a)
# 12:36:04
