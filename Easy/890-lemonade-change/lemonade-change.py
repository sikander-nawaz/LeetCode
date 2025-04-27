class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollars = 0
        ten_dollars = 0
        
        for bill in bills:
            if bill == 5:
                five_dollars += 1
            elif bill == 10:
                if five_dollars > 0:
                    five_dollars -= 1
                    ten_dollars += 1
                else:
                    return False
            elif bill == 20:
                if ten_dollars > 0 and five_dollars > 0:
                    ten_dollars -= 1
                    five_dollars -= 1
                elif five_dollars >= 3:
                    five_dollars -= 3
                else:
                    return False
        
        return True
