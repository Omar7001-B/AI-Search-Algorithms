graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def iddfs(start, target, max_depth):
    for i in range(max_depth + 1):
        result = dls(start, target, i)
        if result is not None:
            return result
    return None

def dls(node, target, depth):
    if node == target:
        return [node]
    if depth == 0:
        return None

    for neighbor in graph.get(node, []):
        result = dls(neighbor, target, depth - 1)
        if result is not None:
            return [node] + result

    return None

start_node = 'A'
target_node = 'F'
max_depth = 3
iddfs_path = iddfs(start_node, target_node, max_depth)

if iddfs_path is not None:
    print("Iterative Deepening Depth-First Search Path:", ' -> '.join(iddfs_path))
else:
    print("No path found within maximum depth limit.")
