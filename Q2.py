class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size
        
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
        self.components -= 1
        return True

def find_min_cost_k_edge_subtree(n, k, edges):
    cost_1_edges = []
    cost_2_edges = []
    cost_1_counts = [0] * n
    for u, v, c in edges:
        if c == 1:
            cost_1_counts[u] += 1
            cost_1_counts[v] += 1
            cost_1_edges.append((u, v))
        else:
            cost_2_edges.append((u, v))

    start_vertex = max(range(n), key=lambda x: cost_1_counts[x])
    
    min_cost = try_build_tree(cost_1_edges, cost_2_edges, k, n, start_vertex, cost_1_counts)

    return min_cost

def try_build_tree(cost_1_edges, cost_2_edges, k, n, start_vertex, cost_1_counts):
    uf = UnionFind(n)
    vertices = {start_vertex}
    edges_used = 0
    cost = 0

    added_cost_1 = True
    while added_cost_1 and edges_used < k:
        added_cost_1 = False
        for u, v in cost_1_edges:
            if edges_used >= k:
                break
            if (u in vertices or v in vertices) and uf.union(u, v):
                edges_used += 1
                cost += 1
                vertices.add(u)
                vertices.add(v)
                added_cost_1 = True

    while edges_used < k:
        best_vertex = max(
            [i for i in range(n) if i not in vertices],
            key=lambda x: cost_1_counts[x],
            default=None
        )
        
        if best_vertex is None:
            break
        added_edge = False
        for u, v in cost_2_edges:
            if edges_used >= k:
                break
            if ((u in vertices and v == best_vertex) or 
                (v in vertices and u == best_vertex)):
                if uf.union(u, v):
                    edges_used += 1
                    cost += 2
                    vertices.add(u)
                    vertices.add(v)
                    added_edge = True
                    added_cost_1 = True
                    while added_cost_1 and edges_used < k:
                        added_cost_1 = False
                        for u1, v1 in cost_1_edges:
                            if edges_used >= k:
                                break
                            if (u1 in vertices or v1 in vertices) and uf.union(u1, v1):
                                edges_used += 1
                                cost += 1
                                vertices.add(u1)
                                vertices.add(v1)
                                added_cost_1 = True
                    break
        
        if not added_edge:
            break
                    
    if edges_used == k:
        return cost
        
    return float('inf')
def main():
    n, k = map(int, input().split())
    edges = []
    for _ in range((n * (n-1)) // 2):
        u, v, c = map(int, input().split())
        edges.append((u, v, c))
    
    result = find_min_cost_k_edge_subtree(n, k, edges)
    print(result)

if __name__ == "__main__":
    main()
