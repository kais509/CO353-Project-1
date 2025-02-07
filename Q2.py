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
    for u, v, c in edges:
        if c == 1:
            cost_1_edges.append((u, v))
        else:
            cost_2_edges.append((u, v))
    min_cost = float('inf')
    for max_cost_1 in range(min(k, len(cost_1_edges)), -1, -1):
        cost = try_build_tree(max_cost_1,cost_1_edges,cost_2_edges,k,n)
        if cost != float('inf'):
            return cost

    return min_cost

def try_build_tree(max_cost_1_edges,cost_1_edges,cost_2_edges,k,n):
    uf = UnionFind(n)
    used_edges = []
    edges_used = 0
    cost = 0
    for u, v in cost_1_edges:
        if edges_used >= k:
            break
        if edges_used >= max_cost_1_edges:
            break
        if edges_used == 0 or any(uf.find(u) == uf.find(x) or uf.find(v) == uf.find(x)                                     for edge in used_edges for x in edge):
            if uf.union(u, v):
                edges_used += 1
                cost += 1
                used_edges.append((u, v)) 

    if edges_used < k:
        for u, v in cost_2_edges:
            if edges_used >= k:
                break
            if edges_used == 0 or any(uf.find(u) == uf.find(x) or uf.find(v) == uf.find(x) 
                                    for edge in used_edges for x in edge):
                if uf.union(u, v):
                    edges_used += 1
                    cost += 2
                    used_edges.append((u, v))
    if edges_used == k:
        vertices = set()
        for edge in used_edges:
            vertices.add(uf.find(edge[0]))
        if len(vertices) == 1:
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
