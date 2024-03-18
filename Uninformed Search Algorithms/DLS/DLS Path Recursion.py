# Global graph and visited variables
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()

def dls(node, target, depth):
    global visited  # Access the global visited set
    if node == target:
        return [node]
    if depth == 0:
        return None

    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result = dls(neighbor, target, depth - 1)
            if result is not None:
                return [node] + result
    return None

start_node = 'A'
target_node = 'F'
max_depth = 3

visited.clear()
dls_path = dls(start_node, target_node, max_depth)

# Output the result
if dls_path is not None:
    print("Depth-Limited Search Path:", ' -> '.join(dls_path))
else:
    print("No path found within maximum depth limit.")
