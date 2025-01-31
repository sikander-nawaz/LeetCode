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
