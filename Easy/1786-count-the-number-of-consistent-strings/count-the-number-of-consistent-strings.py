class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        A = set(list(allowed))
        return sum([A >= set(list(word)) for word in words])