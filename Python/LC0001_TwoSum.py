"""
 You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 You may assume that each input would have exactly one solution, and you may not use the same element twice.
 You can return the answer in any order.

 Example 1:

 Input: nums = [2,7,11,15], target = 9
 Output: [0,1]
 Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

 Example 2:

 Input: nums = [3,2,4], target = 6
 Output: [1,2]

 Example 3:

 Input: nums = [3,3], target = 6
 Output: [0,1]

 Constraints:

 2 <= nums.length <= 104
 -109 <= nums[i] <= 109
 -109 <= target <= 109
 Only one valid answer exists.

 Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

def example_1():
    nums_1 = [2, 7, 11, 15]
    target_1 = 9 # [0, 1]
    for i in range(len(nums_1)):
        for j in range(len(nums_1)):
            if i != j and nums_1[i] + nums_1[j] == target_1:
                return [i, j]

def example_2():
    nums_2 = [3, 2, 4]
    target_2 = 6 # [1, 2]
    for i in range(len(nums_2)):
        for j in range(len(nums_2)):
            if i != j and nums_2[i] + nums_2[j] == target_2:
                return [i, j]

def example_3():
    nums_3 = [3, 3]
    target_3 = 6 # [0, 1]
    for i in range(len(nums_3)):
        for j in range(len(nums_3)):
            if i != j and nums_3[i] + nums_3[j] == target_3:
                return [i, j]

print(example_1())
print(example_2())
print(example_3())
