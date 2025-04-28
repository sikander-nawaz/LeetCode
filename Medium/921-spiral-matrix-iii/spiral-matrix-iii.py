class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = rStart, cStart
        result = []
        step = 1
        direction_index = 0
        cells_to_visit = rows * cols
        
        while len(result) < cells_to_visit:
            for _ in range(step):
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                r += directions[direction_index][0]
                c += directions[direction_index][1]
            
            if direction_index == 1 or direction_index == 3:
                step += 1
            
            direction_index = (direction_index + 1) % 4
        
        return result
