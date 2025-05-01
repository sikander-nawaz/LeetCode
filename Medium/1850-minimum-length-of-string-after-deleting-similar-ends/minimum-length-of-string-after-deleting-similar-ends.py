class Solution:
    def minimumLength(self, s: str) -> int:
        char=s[-1]
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                break
            while left<=right and s[left]==char:
                left+=1
            while left<=right and s[right]==char:
                right-=1
            char=s[right]
        return right-left+1