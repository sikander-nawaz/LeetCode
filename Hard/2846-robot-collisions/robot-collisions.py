class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
    
        stack = []
    
        for position, health, direction, index in robots:
            if direction == 'R':
                stack.append((position, health, direction, index))
            else:  # direction == 'L'
                while stack and stack[-1][2] == 'R':
                    r_position, r_health, r_direction, r_index = stack.pop()
                    if r_health > health:
                        stack.append((r_position, r_health - 1, r_direction, r_index))
                        health = 0
                    elif r_health < health:
                        health -= 1
                    else:
                        health = 0
                    if health == 0:
                        break
                if health > 0:
                    stack.append((position, health, direction, index))
    
    # Sort the surviving robots by their original indices
        surviving_robots = sorted(stack, key=lambda x: x[3])
    
    # Return the healths in the order of their original indices
        return [health for position, health, direction, index in surviving_robots]