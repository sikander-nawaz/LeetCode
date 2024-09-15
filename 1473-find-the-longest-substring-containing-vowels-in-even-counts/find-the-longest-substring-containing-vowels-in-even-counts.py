class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        bitmap = {0: -1}
        max_len = 0
        curr = 0

        for i, ch in enumerate(s):
            if ch in vowels:
                curr ^= (1 << vowels[ch])
            if curr not in bitmap:
                bitmap[curr] = i
            else:
                max_len = max(max_len, i - bitmap[curr])

        return max_len