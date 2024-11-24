class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negativeElementsCount = 0
        minElement = 10e5 + 1
        sumElements = 0
        for row in matrix:
            for cell in row:
                if cell < 0:
                    negativeElementsCount += 1
                    sumElements -= cell
                else:
                    sumElements += cell

                if abs(cell) < minElement:
                    minElement = abs(cell)
        print(sumElements)
        print(negativeElementsCount)
        print(minElement)
        if negativeElementsCount % 2 == 0:
            return sumElements
        else:
            return sumElements - 2*minElement
                
