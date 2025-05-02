class Solution:
    def repeatedCharacter(self, s: str) -> str:
        e_set = set()
        for i in s:
            if i in e_set:
                return i

            e_set.add(i)