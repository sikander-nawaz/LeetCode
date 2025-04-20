class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        # Helper function to perform topological sorting
        def topological_sort(k: int, conditions: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            in_degree = {i: 0 for i in range(1, k + 1)}
            
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            
            queue = deque([node for node in in_degree if in_degree[node] == 0])
            topo_order = []
            
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(topo_order) == k:
                return topo_order
            else:
                return []
        
        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)
        
        if not row_order or not col_order:
            return []
        
        position_map = {num: (row_order.index(num), col_order.index(num)) for num in range(1, k + 1)}
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            row, col = position_map[num]
            matrix[row][col] = num
        
        return matrix
