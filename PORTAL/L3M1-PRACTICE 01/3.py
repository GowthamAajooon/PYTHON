Given an array of elements of length N, ranging from 1 to N, all elements may not be present in the array. 
If element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, 
display -1 at that place. Index starts from 0

Refer to sample input and output for more clarity

Input Format
N - size of the array

'N' integer values

Output Format
Input array in proper arrangement

Sample Input
6
6 1 9 3 2 4
Sample Output
-1 1 2 3 4 -1 6 -1 -1 9 

For example:

Input	        Result
6             0 -1 2 -1 4 -1 6 -1 8 -1 10
0 2 4 6 8 10

5
0 1 2 3 4     0 1 2 3 4 


#PROGRAM

n = int(input())
m = sorted(list(map(int,input().split())))
print(*[i if i in m else -1 for i in range(m[len(m)-1]+1)] )



Input	                        Expected	                             Got	
6
0 2 4 6 8 10                  0 -1 2 -1 4 -1 6 -1 8 -1 10            0 -1 2 -1 4 -1 6 -1 8 -1 10
5
0 1 2 3 4                     0 1 2 3 4                              0 1 2 3 4
Passed all tests!  
