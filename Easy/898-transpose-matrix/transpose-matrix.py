class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)              
        colum = len(matrix[0])       

        result = [[0] * row for _ in range(colum)] 
        
        for i in range(colum):                    
            for j in range(row):
                result[i][j] = matrix[j][i]

        return result