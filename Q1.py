from collections import defaultdict
import heapq

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def dijkstra(graph, start, n):
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > distances[u]:
            continue
        
        for v, w in graph[u]:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                heapq.heappush(pq, (distances[v], v))
                
    return distances

def solve_spanning_trees(n, edges, root):
    # Build adjacency list for Dijkstra
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Calculate shortest paths from root
    distances = dijkstra(graph, root, n)
    
    # Prepare edges for Kruskal's algorithm
    edges_with_closeness = []
    for u, v, w in edges:
        closeness = min(distances[u], distances[v])
        edges_with_closeness.append((closeness, u, v))
    
    # Sort edges by closeness for both MSTs
    edges_with_closeness.sort()
    
    # Find minimum closeness spanning tree
    uf = UnionFind(n)
    min_closeness = 0
    edges_used = 0
    
    for d, u, v in edges_with_closeness:
        if uf.union(u, v):
            min_closeness += d
            edges_used += 1
            if edges_used == n - 1:
                break
    
    # Find maximum closeness spanning tree
    uf = UnionFind(n)
    max_closeness = 0
    edges_used = 0
    
    for d, u, v in reversed(edges_with_closeness):
        if uf.union(u, v):
            max_closeness += d
            edges_used += 1
            if edges_used == n - 1:
                break
    
    return min_closeness, max_closeness

def main():
    # Read input
    n, m, r = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    # Solve and print output
    min_close, max_close = solve_spanning_trees(n, edges, r)
    print(min_close, max_close)

if __name__ == "__main__":
    main()
