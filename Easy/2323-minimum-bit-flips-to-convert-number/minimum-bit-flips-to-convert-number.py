class Solution:
    def minBitFlips(self, s: int, g: int) -> int:
        return (bin(s^g)).count('1')