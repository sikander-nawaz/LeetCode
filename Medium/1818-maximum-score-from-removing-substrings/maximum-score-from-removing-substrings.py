class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_and_score(s, sub, score):
            stack = []
            total_score = 0
        
            for char in s:
                if stack and stack[-1] + char == sub:
                    stack.pop()
                    total_score += score
                else:
                    stack.append(char)
        
            return ''.join(stack), total_score
    
        if x > y:
            # Remove "ab" first, then "ba"
            s, score1 = remove_and_score(s, "ab", x)
            _, score2 = remove_and_score(s, "ba", y)
        else:
        # Remove "ba" first, then "ab"
            s, score1 = remove_and_score(s, "ba", y)
            _, score2 = remove_and_score(s, "ab", x)
    
        return score1 + score2