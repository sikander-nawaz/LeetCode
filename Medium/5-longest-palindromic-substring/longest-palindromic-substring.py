class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) == 0:
            return ""

        longest_palindrome = ""
        for i in range(len(s)):
            # Odd length palindromes
            palindrome1 = expand_around_center(i, i)
            # Even length palindromes
            palindrome2 = expand_around_center(i, i + 1)
            
            # Update longest palindrome if a longer one is found
            if len(palindrome1) > len(longest_palindrome):
                longest_palindrome = palindrome1
            if len(palindrome2) > len(longest_palindrome):
                longest_palindrome = palindrome2

        return longest_palindrome
