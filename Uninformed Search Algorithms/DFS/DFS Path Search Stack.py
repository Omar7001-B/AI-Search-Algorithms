def dfs(graph, start, target):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == target:
            print(visited)
            return path

        visited.add(node)
        for child in reversed(graph.get(node, [])):
            if child not in visited:
                stack.append(path + [child])

    return None

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# DFS
dfs_path = dfs(graph, 'A', 'F')
print("DFS Path:", ' -> '.join(dfs_path) if dfs_path else "No path found with DFS")
