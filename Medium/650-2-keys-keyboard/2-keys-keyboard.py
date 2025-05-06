class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                ans += factor
                n //= factor
            factor += 1
        return ans
