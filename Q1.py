from collections import defaultdict

#o(M LOG N)
def dijkstra():
    #write disktra and then we can check if the output works as the final answer
    return 0


#O(2m)
def solve_spanning_trees(n, edges, root):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    #maybe change how the graph weight is stored/calculated for output

    min_closeness = 0   
    max_closeness = 0

    return min_closeness, max_closeness

def main():
    # Read input
    n, m, r = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
    
    # Solve and print output
    min_close, max_close = solve_spanning_trees(n, edges, r)
    print(min_close, max_close)

if __name__ == "__main__":
    main()
