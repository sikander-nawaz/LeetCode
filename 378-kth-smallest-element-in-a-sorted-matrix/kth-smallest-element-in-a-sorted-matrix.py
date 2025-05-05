class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newArr = sum(matrix, [])
        newArr.sort()
        return newArr[k - 1]
        