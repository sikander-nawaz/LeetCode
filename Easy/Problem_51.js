// You are given an array nums consisting of positive integers.
// Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
// The frequency of an element is the number of occurrences of that element in the array.

// Example 1:
// Input: nums = [1,2,2,3,1,4]
// Output: 4
// Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
// So the number of elements in the array with maximum frequency is 4.

// SOLUTION:


class Solution {
     public int maxFrequencyElements(int[] nums) {
         Map<Integer, Integer> map = new HashMap<>();
         int max = 0;
 
         for(int i = 0; i < nums.length; i++){
             if(map.containsKey(nums[i])){
                 map.put(nums[i], map.get(nums[i]) + 1);
             }else{
                 map.put(nums[i], 1);
             }
             if(map.containsKey(nums[i]) && map.get(nums[i]) > max){
                 max = map.get(nums[i]);
             }
         }
         int count = 0;
         List<Integer> list = new ArrayList<>(map.values());
         for (int num : list){
             if(num == max){
                 count += num;
             }
         }
         return count;
     }
 }