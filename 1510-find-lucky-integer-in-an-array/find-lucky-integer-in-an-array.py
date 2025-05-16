class Solution:
    def findLucky(self, arr: List[int]) -> int:
        array=[-1]
        Set = set(arr)

        for i in arr:
            if arr.count(i) == i:
                array.append(i)
        return max(array)