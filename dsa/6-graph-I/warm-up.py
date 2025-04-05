# graph intro
from collections import deque


def depth_first_traversal(graph, start):
    stack = [ start ]
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for neighbor in reversed(graph[current]):
                stack.append(neighbor)
        
        
def depth_first_traversal_recursive(graph, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_traversal_recursive(graph,neighbor)
        

def breadth_first_print(graph, start):
    queue = deque([start])
    while queue:
        current = queue[0]
        print(current)
        queue.popleft()
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    
    
graph = {
    "a": ["b","c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

print("Printing DFS")
depth_first_traversal(graph,"a")
depth_first_traversal_recursive(graph,"a")
print("Printing BFS")
breadth_first_print(graph,"a")