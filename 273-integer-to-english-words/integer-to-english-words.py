class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                        "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return less_than_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + helper(num % 10)
            elif num < 1000:
                return less_than_20[num // 100] + " Hundred " + helper(num % 100)
            else:
                for i in range(len(thousands)):
                    if num < 1000 ** (i + 1):
                        return helper(num // (1000 ** i)) + thousands[i] + " " + helper(num % (1000 ** i))
        
        return helper(num).strip()

