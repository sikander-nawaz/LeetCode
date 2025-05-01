class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        par = sum(rolls)
        tot = mean * (m + n)
        if tot - par > 6 * n or tot - par < n:
            return []
        a, b = (tot - par) // n, (tot - par) % n
        output = [a] * (n - b) + [a + 1] * b
        return output
        