graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dls(start, target, max_depth):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]
        visited.add(node)

        if node == target:
            return path

        if len(path) <= max_depth:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None

start_node = 'A'
target_node = 'F'
max_depth = 3

dls_path = dls(start_node, target_node, max_depth)

# Output the result
if dls_path is not None:
    print("Depth-Limited Search Path:", ' -> '.join(dls_path))
else:
    print("No path found within maximum depth limit.")
