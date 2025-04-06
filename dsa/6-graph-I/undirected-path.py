# undirected path

# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B).
# The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
from collections import defaultdict


def undirected_path(edges, node_A, node_B):
    # Step 1: Build the graph as an adjacency list
    graph = defaultdict(list)  # Creates a dictionary where each value is initialized as an empty list
    for node1, node2 in edges:
        graph[node1].append(node2)  # Add connection from node1 to node2
        graph[node2].append(node1)  # Add connection from node2 to node1 (undirected)

    # Step 2: Define DFS function to search for a path from current to target
    def dfs(current, target, visited):
        if current == target:
            return True  # Found the target node

        if current in visited:
            return False  # Already visited this node, avoid cycles

        visited.add(current)  # Mark current node as visited

        # Explore all unvisited neighbors
        for neighbor in graph[current]:
            if dfs(neighbor, target, visited):  # Recursive DFS call
                return True  # Found path through this neighbor

        return False  # No path found from this route

    # Start DFS from node_A looking for node_B
    return dfs(node_A, node_B, set())


def build_graph(edges):
  graph = {}
  for edge in edges:
    a,b = edge
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
    
  return graph

graph = {
    "i": ["j","k"],
    "j": ["i"],
    "k": ["i","m","l"],
    "m": ["k"],
    "l": ["k"],
    "o": ["n"],
    "n": ["o"]
}

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True
