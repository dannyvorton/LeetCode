/**
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
 */

public class LC0001_TwoSum {

  public static int[] example1() {
    int[] num = {2, 7, 11, 15};
    int target = 9;
    for (int i = 0; i < num.length; i++) {
      for (int j = i + 1; j < num.length; j++) {
        if (num[i] + num[j] == target) {
          return new int[] {i, j};
        }
      }
    }
    return new int[] {};
  }

  public static void example2() {
    int[] num = {3, 2, 4};
    int target = 6;
  }

  public static void example3() {
    int[] num = {3, 3};
    int target = 6;
  }

  public static void main(String[] args) {
    example1();
    example2();
    example3();
  }

}
