Given an unsorted list of integers, square the elements and give the output in sorted order.

Input Format

5 

-9 -2 0 2 3

Constraints

1 <= N <= 100 0 <= arr[i] <= 10000

Output Format

0 4 4 9 81



# PROGRAM
n = int(input())
l = list(map(int,input().split()))
l1 = [i*i for i in l]
print(*sorted(l1))



Input	                        Expected	                Got	
5
-9 -2 0 2 3                   0 4 4 9 81                0 4 4 9 81


#---------------------------------------------------------------------------------------------------------------

Convert the array into zig-zag order. The converted array should be formatted in this

pattern a < b > c < d > e < f

First the number of elements in the array N is provided followed by each of the numbers.

Input Format

First line is N, size of array. 1<=N<=100

Constraints

1<=N<=100

Output Format

An array with zigzag pattern

Example
Input

5

31

32

33

34

35

output

[31, 33, 32, 35, 34]

# PROGRAM

arr =[int(input()) for i in range(int(input()))]
f = []
f.append(arr[0])
arr.pop(0)
for i in range(len(arr)//2):
    f.append(arr[1])
    f.append(arr[0])
    arr.pop(1)
    arr.pop(0)
print(f)
        
  
  
  
Input	                            Expected	                            Got	
5
31
32
33
34
35                              [31, 33, 32, 35, 34]                    [31, 33, 32, 35, 34]


#----------------------------------------------------------------------------------------------------

Write a program to print all the LEADERS in the array.

Note: An element is leader if it is greater than all the elements to its right side.


For example:

Input	                              Result
8
12 15 75 9 59 6 47 23               75 59 47 23 
4
212 45 76 95                        212 95


# PROGRAM
n = int(input())
a = list(map(int,input().split()))
for i in range(len(a)):
    if max(a[i:])==a[i]:
        print(a[i],end=" ")




Input	                             Expected	                        Got	
8
12 15 75 9 59 6 47 23              75 59 47 23                      75 59 47 23
4
212 45 76 95                       212 95                           212 95



#------------------------------------------------------------------------------------
A personal identification number (PIN) is a numeric or alphanumeric password or code used in the process of authenticating or identifying a user. The PIN numbers of the customers of FB Bank are encoded in an array. Your task is to decode the array and generate the six digit PIN number based on the following rules:

1. Find the cumulative sum of all the digits until you get a single digit.

2. Replace all the odd numbers with their respective alphabets in lowercase i.e.

1=a, 2=b...9=i...



Explanation:

pinArray = { 1, 22, 123, 4242, 45, 56 }

the cumulative sums are

= { 1, 4, 6, 3, 9, 2 }

= 146392

After replacing all the odd numbers with alphabets

Output = a46ci2


Input	                      Result
6
14 18 6 548 46 78           ei68a6
6
0 1 2 8 45 5896             0a28ia




#PROGRAM 
n = int(input())
f = list(map(str,input().split()))
for i in range(len(f)):
    while len(f[i])!=1:
        f[i] = str(sum(map(int,f[i])))
    if int(f[i])%2!=0:
        print(chr(96+int(f[i])),end="")
    else:
        print(f[i],end="")
        
        
Input	                    Expected	              Got	
6
14 18 6 548 46 78         ei68a6                  ei68a6
6
0 1 2 8 45 5896           0a28ia                  0a28ia




















