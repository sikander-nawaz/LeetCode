class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        result = float('inf')
        dq = collections.deque()
        
        for right in range(n + 1):
            # Find valid subarrays and update result
            while dq and prefix[right] - prefix[dq[0]] >= k:
                result = min(result, right - dq[0])
                dq.popleft()
            
            # Maintain monotonic increasing deque
            while dq and prefix[right] <= prefix[dq[-1]]:
                dq.pop()
                
            dq.append(right)
        
        return result if result != float('inf') else -1
