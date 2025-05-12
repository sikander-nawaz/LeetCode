class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        unique_palindromes = set()

        # Arrays to track the first and last occurrence of each character
        first = [-1] * 26
        last = [-1] * 26

        # Populate first and last occurrence arrays
        for i, char in enumerate(s):
            index = ord(char) - ord('a')
            if first[index] == -1:
                first[index] = i
            last[index] = i

        # Iterate over all lowercase letters
        for i in range(26):
            if first[i] != -1 and last[i] != -1 and first[i] < last[i]:
                # Collect unique characters between first[i] and last[i]
                middle_chars = set(s[first[i] + 1:last[i]])
                # Create palindromic subsequences
                for char in middle_chars:
                    palindrome = chr(i + ord('a')) + char + chr(i + ord('a'))
                    unique_palindromes.add(palindrome)

        return len(unique_palindromes)