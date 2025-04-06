# has path

# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed
# acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not
# there exists a directed path between the source and destination nodes.
from collections import deque


def has_path_dfs_recursive(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph.get(src, []):
        
        if has_path_dfs_recursive(graph, neighbor, dst):
            return True
        
    return False


def has_path_dfs(graph, src, dst):
    if src == dst:
        return True

    stack = deque([src])

    while stack:
        current = stack.pop()

        if current == dst:
            return True

        for neighbor in graph.get(current, []):
            stack.append(neighbor)

    return False


graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

print(has_path_dfs(graph, "f", "k"))  # True
print(has_path_dfs(graph, "f", "j"))  # ➞ False
print(has_path_dfs_recursive(graph, "f", "k"))  # True
print(has_path_dfs_recursive(graph, "f", "j"))  # ➞ False
