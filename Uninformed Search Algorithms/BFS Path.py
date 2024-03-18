graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}


def bfs(start, target):
    visited = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == target:
            print("Path: ",  ' - > '.join(path))
            print(path)
        if node not in visited:
            visited.append(node)
            for child in graph.get(node, []):
                queue.append(path + [child])
    print(visited)

bfs('A', 'F')

