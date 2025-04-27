# start code
class Solution:
    def diffWaysToCompute(self, expression: str):
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, ch in enumerate(expression):
            if ch in '+-*':
                for l in self.diffWaysToCompute(expression[:i]):
                    for r in self.diffWaysToCompute(expression[i+1:]):
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        elif ch == '*':
                            res.append(l * r)
        return res
