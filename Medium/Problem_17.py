# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

# You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

# Example 1:
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert the string "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.
# - Change value at index 2 from 'c' to 'e' at a cost of 1.
# - Change value at index 2 from 'e' to 'b' at a cost of 2.
# - Change value at index 3 from 'd' to 'e' at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.


# SOLUTION:

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        if len(target) != n:
            return -1
        
        # Number of lowercase English letters
        ALPHABET_SIZE = 26
        
        # Initialize the cost matrix with infinity
        inf = sys.maxsize
        cost_matrix = [[inf] * ALPHABET_SIZE for _ in range(ALPHABET_SIZE)]
        
        # Fill the diagonal with 0
        for i in range(ALPHABET_SIZE):
            cost_matrix[i][i] = 0
        
        # Populate the cost matrix with the given transformations
        for i in range(len(cost)):
            x = ord(original[i]) - ord('a')
            y = ord(changed[i]) - ord('a')
            cost_matrix[x][y] = min(cost_matrix[x][y], cost[i])
        
        # Floyd-Warshall algorithm to find minimum cost for all pairs
        for k in range(ALPHABET_SIZE):
            for i in range(ALPHABET_SIZE):
                for j in range(ALPHABET_SIZE):
                    if cost_matrix[i][k] < inf and cost_matrix[k][j] < inf:
                        cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        
        # Calculate the total minimum cost to convert source to target
        total_cost = 0
        for i in range(n):
            if source[i] == target[i]:
                continue
            src_char = ord(source[i]) - ord('a')
            tgt_char = ord(target[i]) - ord('a')
            if cost_matrix[src_char][tgt_char] == inf:
                return -1
            total_cost += cost_matrix[src_char][tgt_char]
        
        return total_cost
