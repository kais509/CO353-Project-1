from collections import defaultdict


def dijkstra(graph, start, n):
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    visited = set()
    parent = {i: None for i in range(n)}  
    # Priority queue to store vertices and their distances
    pq = [(0, start)]
    
    while pq:
        # Get vertex with minimum distance
        curr_dist, curr_vertex = min(pq)
        pq.remove((curr_dist, curr_vertex))
        
        # Skip if already visited
        if curr_vertex in visited:
            continue
            
        # Mark as visited
        visited.add(curr_vertex)
        
        # Check all neighbors
        for neighbor, weight in graph[curr_vertex]:
            if neighbor not in visited:
                distance = curr_dist + weight
                
                # Update if shorter path found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parent[neighbor] = curr_vertex  # Track the parent
                    pq.append((distance, neighbor))
    
    # Construct the tree edges
    tree_edges = []
    for vertex in range(n):
        if vertex != start and parent[vertex] is not None:
            # Find the weight of this edge from the original graph
            weight = next(w for v, w in graph[parent[vertex]] if v == vertex)
            tree_edges.append((parent[vertex], vertex, weight))
                    
    return distances, tree_edges


#O(2m)
def solve_spanning_trees(n, edges, root):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    #maybe change how the graph weight is stored/calculated for output

    distances, tree_edges = dijkstra(graph, root, n)  # Updated to unpack both return values
    print("Distances:", distances)
    print("Shortest path tree edges:", tree_edges)

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
