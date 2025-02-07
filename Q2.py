class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size  # Only needed feature beyond Q1's version
        
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
    for max_cost_1 in range(min(k + 1, len(cost_1_edges) + 1)):
        cost = try_build_tree(max_cost_1,n,k,cost_1_edges,cost_2_edges)
        min_cost = min(min_cost, cost)
    
    return min_cost

def try_build_tree(max_cost_1_edges,n,k,cost_1_edges,cost_2_edges):
    uf = UnionFind(n)
    edges_used = 0
    cost = 0
    
    for u, v in cost_1_edges:
        if edges_used >= k:
            break
        if edges_used >= max_cost_1_edges:
            break
        if uf.union(u, v):
            edges_used += 1
            cost += 1
    
    if edges_used < k:
        for u, v in cost_2_edges:
            if edges_used >= k:
                break
            if uf.union(u, v):
                edges_used += 1
                cost += 2
    
    if edges_used == k and uf.components == n - edges_used:
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