visited = set()
def dfs(start, target , path=[]):
    visited.add(start)
    path = path + [start]
    if start == target:
        return path
    for child in graph[start] - visited:
        new_path = dfs(child, target, path)
        if new_path:
            return new_path
    return None

# Example graph
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Starting and target nodes
start_node, target_node = 'A', 'F'

# DFS
dfs_path = dfs(start_node, target_node)
print("DFS Path:", ' -> '.join(dfs_path) if dfs_path else "No path found with DFS")
