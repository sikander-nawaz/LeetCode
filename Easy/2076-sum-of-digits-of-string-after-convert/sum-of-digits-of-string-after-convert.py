class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        for i in range(0, len(s)):
            string += str(ord(s[i])-96)
        
        sum = 0
        for x in range(0, k):
            sum = 0
            for i in range(0, len(string)):
                sum += int(string[i])
            string = str(sum)
        return sum