import heapq
from collections import defaultdict
class Solution:

    def dijkstra(
        self, start: int, end: int,
        adj_list: dict[int, list[tuple[int, int]]], paths: list[set[int]],
        costs: list[int], boundary: int
    ) -> None:
        seen: set[int] = set()
        heap: list[tuple[int, int]] = [(0, start)]
        costs[start] = 0

        while heap:
            cur_weight, cur_vertex = heapq.heappop(heap)
            if cur_vertex in seen: continue
            seen.add(cur_vertex)
            if cur_weight > boundary: return
            if cur_vertex == end: return
            for neighbor in adj_list.get(cur_vertex, []):
                neighbor_weight, neighbor_vertex = neighbor
                if cur_weight + neighbor_weight < costs[neighbor_vertex]:

                    costs[neighbor_vertex] = cur_weight + neighbor_weight
                    paths[neighbor_vertex].clear()
                    paths[neighbor_vertex].update(paths[cur_vertex])
                    paths[neighbor_vertex].add((cur_vertex, neighbor_vertex))

                heapq.heappush(heap, (cur_weight + neighbor_weight, neighbor_vertex))
                    

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        should_be_changed: set[int] = set()
        adj_list: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for idx in range(len(edges)):
            edge: list[int, int, int] = edges[idx]
            start, end, weight = edge
            if weight == -1:
                should_be_changed.add((start, end))
                edge[2] = 1
                weight = edge[2]
            adj_list[start].append((weight, end))
            adj_list[end].append((weight, start))

        for _ in range(n):     
            paths: list[set[int]] = [set() for _ in range(n)]
            costs: list[int] = [float('inf')] * n
            self.dijkstra(source, destination, adj_list, paths, costs, target)
            if costs[destination] >= target: break

            for idx in range(len(edges)):
                edge: list[int, int, int] = edges[idx]
                if (
                    (edge[0], edge[1]) in should_be_changed and
                    (
                        (edge[0], edge[1]) in paths[destination] or
                        (edge[1], edge[0]) in paths[destination]
                    )
                ):
                    edge[2] += target - costs[destination]
                    for ceil_idx in range(len(adj_list[edge[0]])):
                        if adj_list[edge[0]][ceil_idx][1] == edge[1]:
                            adj_list[edge[0]][ceil_idx] = (edge[2], edge[1])                  
                            break
                    for ceil_idx in range(len(adj_list[edge[1]])):
                        if adj_list[edge[1]][ceil_idx][1] == edge[0]:
                            adj_list[edge[1]][ceil_idx] = (edge[2], edge[0])                  
                            break
                    
                    break

        return edges if costs[destination] == target else []