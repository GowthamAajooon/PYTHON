Given a string s, find the first non-repeating character in it and return its position. If it does not exist, return -1.

 

Example 1:

Input: s = "itvac"
Output: 1
Example 2:

Input: s = "lovecodinglife"
Output: 3
Example 3:

Input: s = "aabb"
Output: -1


For example:

Input	  Result
itvac   1


# PROGRAM 

from collections import Counter
h = input()
s = Counter(h)
for k,i in s.items():
    if i==1:
        print(h.index(k)+1)
        break
else:
    print("-1")
    
    
    
Input	              Expected	        Got	
itvac               1                 1
lovecodinglife      3                 3


#--------------------------------------------------------------------------------------------------------------------



Develop a program to print ascending and descending of a number

Example

5

1 5 2 4 3 3 4 2 5 1



In the above, alternate numbers are ascending 1 to 5 and alternate numbers are descending from 5 to 1

Constraints

1<=N<=1000




For example:

Input	            Result
5                 1 5 2 4 3 3 4 2 5 1


# PROGRAM 

n = [i for i in range(1,int(input())+1)]
if len(n)%2!=0:
    j,f = 1,[]
    for i in range(len(n)//2):
        f.append(n[i])
        f.append(n[len(n)-j])
        j+=1
    f.append(n[len(n)//2])
    print(*(f+f[::-1]))
else:
    j,f = 1,[]
    for i in range(len(n)//2):
        f.append(n[i])
        f.append(n[len(n)-j])
        j+=1
    print(*(f+f[::-1]))
    
    
    
Input	                Expected	                  Got	
5                     1 5 2 4 3 3 4 2 5 1         1 5 2 4 3 3 4 2 5 1

#---------------------------------------------------------------------------------------



Left Rotation and Right Rotation of a String
Given a string of size n, write functions to perform the following operations on a string-

Left (Or anticlockwise) rotate the given string by d elements (where d <= n)
Right (Or clockwise) rotate the given string by d elements (where d <= n).
Examples: 

Input : s = "srishakthi"
        d = 2
Output : Left Rotation  : "ishakthisr" 
         Right Rotation : "hisrishakt" 
Input : s = "qwertyu" 
        d = 2
Output : Left rotation : "ertyuqw"
         Right rotation : "yuqwert"


For example:

Input	                    Result
srishakthi                Left Rotation:"ishakthisr"
2                         Right Rotation:"hisrishakt" 

# PROGRAM

f = input()
n = int(input())
print("Left Rotation:"+'"'+f[n:]+f[:n]+'"')
print("Right Rotation:"+'"'+f[len(f)-n:]+f[:len(f)-n]+'"')


Input	                            Expected	                        Got	
srishakthi                        Left Rotation:"ishakthisr"        Left Rotation:"ishakthisr"
2                                 Right Rotation:"hisrishakt"       Right Rotation:"hisrishakt"

                                 
#---------------------------------------------------------------------------------------------------------------


Write a program to reverse the words in a given sentence.

Input Format

This is a word

Output Format

sihT si a drow


For example:

Input	              Result
This is a word      sihT si a drow

# PROGRAM
n = input().split()
print(*[i[::-1] for i in n ])

Input	            Expected	            Got	
This is a word    sihT si a drow        sihT si a drow




                                                                    


