class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordsCount = Counter((s1 + " " + s2).split())

        return [k for k, v in wordsCount.items() if v == 1]
        