class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rd = [] # empty stack to keep scores
        for o in ops:
            if o == '+':
                rd.append(rd[-1] + rd[-2])
            elif o == 'D':
                rd.append(rd[-1]*2)
            elif o == "C":
                rd.pop()
            else:
                rd.append(int(o))
        return sum(rd)