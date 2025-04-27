from collections import deque

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