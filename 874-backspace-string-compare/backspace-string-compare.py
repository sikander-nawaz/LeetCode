class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):

            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        
        
        return backspace(s) == backspace(t)