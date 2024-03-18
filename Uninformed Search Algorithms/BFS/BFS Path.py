def bfs(graph, start, target):
    visited = set()
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == target:
            return path

        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(path + [neighbor])

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

# BFS
bfs_path = bfs(graph, 'A', 'F')
print("BFS Path:", ' -> '.join(bfs_path) if bfs_path else "No path found with BFS")
