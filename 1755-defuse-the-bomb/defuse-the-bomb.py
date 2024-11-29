class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        s, ans = 0, []
        if k < 0:
            for i in range(k, n):
                if i >= 0:
                    ans.append(s)
                    s -= code[i+k]
                s += code[i]
            return ans

        for i in range(n+k):
            s += code[i%n]
            if i >= k:
                s -= code[i-k]
                ans.append(s)     
        return ans