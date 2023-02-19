Write a program to sort the elements in odd positions in descending order and elements in even position ascending order Example: Input: 1,2,3,4,5,6,7,8,9 Output: 9,2,7,4,5,6,3,8,1

Input Format

First line- N, number of elements Next N line- array elements

Constraints

1

Output Format

Modified Array

Sample Input 0

10
1 2 3 4 5 6 7 8 9 10
Sample Output 0

9 2 7 4 5 6 3 8 1 10


# PROGRAM

n = int(input())
l = list(map(int,input().split()))
c1,c2 = l[::2][::-1],l[1::2]
print("".join( str(c1[i])+" "+str(c2[i])+" " for i in range(len(c1))))


Input	                 Expected	              Got	
10
1 2 3 4 5 6 7 8 9 10   9 2 7 4 5 6 3 8 1 10   9 2 7 4 5 6 3 8 1 10
Passed all tests!  
