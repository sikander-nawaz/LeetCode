/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    if (!nums.includes(target)) {
        return [-1, -1];
    } else {
        let firstPosition = nums.indexOf(target);
        let lastPosition = nums.lastIndexOf(target);
        return [firstPosition, lastPosition];
    }
};