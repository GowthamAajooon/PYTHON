Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: 1,1,2
Output: 1,2
Example 2:
Input: 0,0,1,1,1,2,2,3,3,4
Output: 0,1,2,3,4
Constraints:

0 <= nums length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order


#PROGRAM
print(str(sorted(set(input().split(",")))).replace("', '",",").replace("['","").replace("']",""))





Input	                      Expected	                    Got	
1,1,2                       1,2                           1,2
0,0,1,1,1,2,2,3,3,4         0,1,2,3,4                     0,1,2,3,4
10,11,12,13,14              10,11,12,13,14                10,11,12,13,14
Passed all tests!  
