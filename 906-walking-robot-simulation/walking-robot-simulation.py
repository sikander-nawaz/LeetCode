class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obst_set = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        x, y = 0, 0
        dir_idx = 0
        max_distance_sq = 0
        
        for command in commands:
            if command == -1:
                dir_idx = (dir_idx + 1) % 4
            elif command == -2:
                dir_idx = (dir_idx - 1) % 4
            else:
                dx, dy = directions[dir_idx]
                for _ in range(command):
                    if (x + dx, y + dy) not in obst_set:
                        x += dx
                        y += dy
                        max_distance_sq = max(max_distance_sq, x ** 2 + y ** 2)
                    else:
                        break
        
        return max_distance_sq
