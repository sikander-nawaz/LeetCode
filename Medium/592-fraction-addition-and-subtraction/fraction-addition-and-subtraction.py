from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        result = Fraction(0, 1)
        
        i, n = 0, len(expression)
        
        while i < n:
            if expression[i] in '+-':
                sign = 1 if expression[i] == '+' else -1
                i += 1
            else:
                sign = 1
            
            numerator = 0
            while i < n and expression[i].isdigit():
                numerator = numerator * 10 + int(expression[i])
                i += 1
            
            i += 1
            
            denominator = 0
            while i < n and expression[i].isdigit():
                denominator = denominator * 10 + int(expression[i])
                i += 1
            
            fraction = Fraction(sign * numerator, denominator)
            result += fraction
        
        numerator, denominator = result.numerator, result.denominator
        return f"{numerator}/{denominator}"
