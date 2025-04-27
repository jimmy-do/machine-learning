from collections import deque
# shortest path

# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
# The function should return the length of the shortest path between A and B. Consider the length as the number of edges 
# in the path, not the number of nodes. If there is no path between A and B, then return -1. You can assume that A and B 
# exist as nodes in the graph.

def shortest_path(edges, current_node, target_node):
  graph = build_graph(edges)
  queue = deque([ (current_node, 0) ])
  visited = set()

  while queue:
    current_node, distance = queue.popleft()
    if current_node == target_node:
      return distance

    for neighbor in graph[current_node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(( neighbor, distance + 1 ))

  return -1


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

edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w','z'))