class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        uniques = set()
        queue = deque()
        cur_sum = 0
        max_sum = 0

        for num in nums:
            if num not in uniques:
                uniques.add(num)
                queue.append(num)
                cur_sum += num
            else:
                while queue[0] != num:
                    top = queue.popleft()
                    uniques.remove(top)
                    cur_sum -= top
                top = queue.popleft()
                queue.append(num)
            if len(uniques) == k:
                max_sum = max(max_sum, cur_sum)
                top = queue.popleft()
                uniques.remove(top)
                cur_sum -= top
        return max_sum